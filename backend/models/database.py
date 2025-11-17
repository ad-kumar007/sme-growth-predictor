"""
Database module for storing prediction history
Uses SQLite for simplicity and portability
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional


class PredictionDatabase:
    """Handles all database operations for prediction history"""
    
    def __init__(self, db_path: str = "predictions.db"):
        self.db_path = Path(__file__).parent.parent / db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database and create tables if they don't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                prediction TEXT NOT NULL,
                confidence_high REAL NOT NULL,
                confidence_medium REAL NOT NULL,
                confidence_low REAL NOT NULL,
                input_data TEXT NOT NULL,
                enterprise_size TEXT,
                enterprise_age INTEGER
            )
        ''')
        
        conn.commit()
        conn.close()
        print(f"✓ Database initialized at {self.db_path}")
    
    def save_prediction(
        self,
        prediction: str,
        confidence_scores: Dict[str, float],
        input_data: Dict
    ) -> int:
        """
        Save a prediction to the database
        
        Returns:
            prediction_id: ID of the saved prediction
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO predictions (
                prediction,
                confidence_high,
                confidence_medium,
                confidence_low,
                input_data,
                enterprise_size,
                enterprise_age
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            prediction,
            confidence_scores.get('High', 0.0),
            confidence_scores.get('Medium', 0.0),
            confidence_scores.get('Low', 0.0),
            json.dumps(input_data),
            input_data.get('Small/Medium/Large'),
            input_data.get('Enterprise_Age')
        ))
        
        prediction_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return prediction_id
    
    def get_all_predictions(self, limit: int = 100) -> List[Dict]:
        """Get all predictions with optional limit"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM predictions
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (limit,))
        
        rows = cursor.fetchall()
        conn.close()
        
        predictions = []
        for row in rows:
            predictions.append({
                'id': row['id'],
                'timestamp': row['timestamp'],
                'prediction': row['prediction'],
                'confidence_scores': {
                    'High': row['confidence_high'],
                    'Medium': row['confidence_medium'],
                    'Low': row['confidence_low']
                },
                'input_data': json.loads(row['input_data']),
                'enterprise_size': row['enterprise_size'],
                'enterprise_age': row['enterprise_age']
            })
        
        return predictions
    
    def get_prediction_by_id(self, prediction_id: int) -> Optional[Dict]:
        """Get a specific prediction by ID"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM predictions WHERE id = ?', (prediction_id,))
        row = cursor.fetchone()
        conn.close()
        
        if not row:
            return None
        
        return {
            'id': row['id'],
            'timestamp': row['timestamp'],
            'prediction': row['prediction'],
            'confidence_scores': {
                'High': row['confidence_high'],
                'Medium': row['confidence_medium'],
                'Low': row['confidence_low']
            },
            'input_data': json.loads(row['input_data']),
            'enterprise_size': row['enterprise_size'],
            'enterprise_age': row['enterprise_age']
        }
    
    def get_statistics(self) -> Dict:
        """Get overall prediction statistics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Total predictions
        cursor.execute('SELECT COUNT(*) FROM predictions')
        total = cursor.fetchone()[0]
        
        # Distribution by prediction
        cursor.execute('''
            SELECT prediction, COUNT(*) as count
            FROM predictions
            GROUP BY prediction
        ''')
        distribution = {row[0]: row[1] for row in cursor.fetchall()}
        
        # Average confidence by prediction type
        cursor.execute('''
            SELECT 
                prediction,
                AVG(CASE 
                    WHEN prediction = 'High' THEN confidence_high
                    WHEN prediction = 'Medium' THEN confidence_medium
                    WHEN prediction = 'Low' THEN confidence_low
                END) as avg_confidence
            FROM predictions
            GROUP BY prediction
        ''')
        avg_confidence = {row[0]: row[1] for row in cursor.fetchall()}
        
        # Distribution by enterprise size
        cursor.execute('''
            SELECT enterprise_size, COUNT(*) as count
            FROM predictions
            WHERE enterprise_size IS NOT NULL
            GROUP BY enterprise_size
        ''')
        size_distribution = {row[0]: row[1] for row in cursor.fetchall()}
        
        # Recent predictions (last 7 days)
        cursor.execute('''
            SELECT COUNT(*) FROM predictions
            WHERE timestamp >= datetime('now', '-7 days')
        ''')
        recent_count = cursor.fetchone()[0]
        
        conn.close()
        
        # Calculate percentages
        percentages = {}
        if total > 0:
            for pred, count in distribution.items():
                percentages[pred] = (count / total) * 100
        
        return {
            'total_predictions': total,
            'distribution': distribution,
            'percentages': percentages,
            'average_confidence': avg_confidence,
            'size_distribution': size_distribution,
            'recent_predictions_7days': recent_count
        }
    
    def delete_prediction(self, prediction_id: int) -> bool:
        """Delete a prediction by ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM predictions WHERE id = ?', (prediction_id,))
        deleted = cursor.rowcount > 0
        
        conn.commit()
        conn.close()
        
        return deleted
    
    def clear_all_predictions(self):
        """Clear all predictions (use with caution!)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM predictions')
        
        conn.commit()
        conn.close()


# Global database instance
_db_instance = None


def get_database() -> PredictionDatabase:
    """Get or create the global database instance"""
    global _db_instance
    if _db_instance is None:
        _db_instance = PredictionDatabase()
    return _db_instance

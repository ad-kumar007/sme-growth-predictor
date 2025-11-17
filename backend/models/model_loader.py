"""
ML Model Loader
Loads the trained SME growth prediction model and provides prediction functionality
"""

import pickle
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.base import BaseEstimator, TransformerMixin


class FeatureSelector(BaseEstimator, TransformerMixin):
    """Custom transformer for feature selection (required for unpickling)"""
    def __init__(self, indices):
        self.indices = indices
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X[:, self.indices]


class SMEGrowthPredictor:
    """Wrapper class for SME Growth Prediction Model"""
    
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model_package = None
        self.pipeline = None
        self.label_encoder = None
        self.label_map = None
        self.numeric_features = None
        self.categorical_features = None
        self.load_model()
    
    def load_model(self):
        """Load the pickled model and extract components"""
        try:
            with open(self.model_path, 'rb') as f:
                self.model_package = pickle.load(f)
            
            self.pipeline = self.model_package['pipeline']
            
            # Fix for scikit-learn version compatibility
            if hasattr(self.pipeline, 'named_steps') and 'preprocessor' in self.pipeline.named_steps:
                preprocessor = self.pipeline.named_steps['preprocessor']
                if not hasattr(preprocessor, '_name_to_fitted_passthrough'):
                    preprocessor._name_to_fitted_passthrough = {}
            
            self.label_encoder = self.model_package['label_encoder']
            self.label_map = self.model_package['label_map']
            
            preprocessing_info = self.model_package['preprocessing_info']
            self.numeric_features = preprocessing_info['numeric_features']
            self.categorical_features = preprocessing_info['categorical_features']
            
            print(f"✓ Model loaded successfully from {self.model_path}")
            print(f"✓ Numeric features: {len(self.numeric_features)}")
            print(f"✓ Categorical features: {len(self.categorical_features)}")
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Model file not found at {self.model_path}")
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")
    
    def get_required_features(self):
        """Return list of all required input features"""
        return {
            'numeric': self.numeric_features,
            'categorical': self.categorical_features,
            'all': self.numeric_features + self.categorical_features
        }
    
    def validate_input(self, data: dict) -> tuple:
        """Validate input data has all required features"""
        all_features = self.numeric_features + self.categorical_features
        missing_features = [f for f in all_features if f not in data]
        
        if missing_features:
            return False, f"Missing required features: {missing_features}"
        
        return True, "Valid"
    
    def preprocess_input(self, data: dict) -> pd.DataFrame:
        """Convert input dict to DataFrame with correct feature order"""
        # Create DataFrame with all features in correct order
        all_features = self.numeric_features + self.categorical_features
        df_data = {feat: [data[feat]] for feat in all_features}
        df = pd.DataFrame(df_data)
        
        # Convert numeric features to float
        for feat in self.numeric_features:
            df[feat] = pd.to_numeric(df[feat], errors='coerce')
        
        # Convert categorical features to string
        for feat in self.categorical_features:
            df[feat] = df[feat].astype(str)
        
        return df
    
    def predict(self, data: dict) -> dict:
        """
        Make prediction on input data
        
        Args:
            data: Dictionary with all required features
        
        Returns:
            Dictionary with prediction and confidence scores
        """
        # Validate input
        is_valid, message = self.validate_input(data)
        if not is_valid:
            raise ValueError(message)
        
        # Preprocess input
        df = self.preprocess_input(data)
        
        # Make prediction
        prediction_encoded = self.pipeline.predict(df)[0]
        prediction_label = self.label_encoder.inverse_transform([prediction_encoded])[0]
        
        # Get confidence scores
        probabilities = self.pipeline.predict_proba(df)[0]
        confidence_scores = {
            label: float(probabilities[i])
            for i, label in enumerate(self.label_encoder.classes_)
        }
        
        return {
            'prediction': prediction_label,
            'confidence_scores': confidence_scores,
            'prediction_encoded': int(prediction_encoded)
        }
    
    def get_model_info(self) -> dict:
        """Return model metadata and performance metrics"""
        return {
            'label_mapping': self.label_map,
            'numeric_features': self.numeric_features,
            'categorical_features': self.categorical_features,
            'performance': self.model_package.get('performance', {}),
            'best_params': self.model_package.get('best_params', {})
        }


# Global model instance (loaded once at startup)
_model_instance = None


def get_model() -> SMEGrowthPredictor:
    """Get or create the global model instance"""
    global _model_instance
    if _model_instance is None:
        model_path = Path(__file__).parent.parent.parent / "ml_model" / "sme_digitalization_model_final.pkl"
        _model_instance = SMEGrowthPredictor(str(model_path))
    return _model_instance

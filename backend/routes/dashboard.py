"""
Dashboard API Routes
Handles prediction history, statistics, and reports
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from models.database import get_database
from utils.pdf_generator import generate_prediction_report
from typing import List

router = APIRouter()


@router.get("/stats")
async def get_statistics():
    """Get overall prediction statistics"""
    try:
        db = get_database()
        stats = db.get_statistics()
        return {
            "status": "success",
            "statistics": stats
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history")
async def get_prediction_history(limit: int = 50):
    """Get prediction history with optional limit"""
    try:
        db = get_database()
        predictions = db.get_all_predictions(limit=limit)
        return {
            "status": "success",
            "count": len(predictions),
            "predictions": predictions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/prediction/{prediction_id}")
async def get_prediction_detail(prediction_id: int):
    """Get details of a specific prediction"""
    try:
        db = get_database()
        prediction = db.get_prediction_by_id(prediction_id)
        
        if not prediction:
            raise HTTPException(status_code=404, detail="Prediction not found")
        
        return {
            "status": "success",
            "prediction": prediction
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/report/{prediction_id}")
async def download_prediction_report(prediction_id: int):
    """Generate and download PDF report for a prediction"""
    try:
        db = get_database()
        prediction = db.get_prediction_by_id(prediction_id)
        
        if not prediction:
            raise HTTPException(status_code=404, detail="Prediction not found")
        
        # Generate PDF
        pdf_buffer = generate_prediction_report(prediction)
        
        # Return as downloadable file
        return StreamingResponse(
            pdf_buffer,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f"attachment; filename=sme_prediction_report_{prediction_id}.pdf"
            }
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating report: {str(e)}")


@router.delete("/prediction/{prediction_id}")
async def delete_prediction(prediction_id: int):
    """Delete a prediction from history"""
    try:
        db = get_database()
        deleted = db.delete_prediction(prediction_id)
        
        if not deleted:
            raise HTTPException(status_code=404, detail="Prediction not found")
        
        return {
            "status": "success",
            "message": f"Prediction {prediction_id} deleted successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/clear-history")
async def clear_all_history():
    """Clear all prediction history (use with caution!)"""
    try:
        db = get_database()
        db.clear_all_predictions()
        return {
            "status": "success",
            "message": "All prediction history cleared"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

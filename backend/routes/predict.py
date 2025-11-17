"""
Prediction API Routes
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Optional
from models.model_loader import get_model
from models.database import get_database

router = APIRouter()


class PredictionRequest(BaseModel):
    """Request model for prediction endpoint"""
    Location: float = Field(..., description="Location code")
    About_Enterprises_Owners_Motivation: int = Field(..., alias="About Enterprises, Owners Motivation")
    Enabler_2_Operational_Process: int = Field(..., alias="Enabler 2:Operational Process , Legacy & new machine to balance")
    Enabler_1_Effortable_Digital_technologies: int = Field(..., alias="Enabler 1: Effortable Digital technologies")
    Outcome_Growth_and_Effeciency: float = Field(..., alias="Outcome : Growth and Effeciency")
    Enabler_2_Certification_Standarization: int = Field(..., alias="Enabler 2 :Certification &Standarization")
    Challanges3_Financial_assistant: int = Field(..., alias="Challanges3: Financial assistant & Incentive ,transparency in institutional support ,")
    Enabler_3_Administrative_Regulatory: int = Field(..., alias="Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges")
    Enabler_4_Engaging_local_hire: int = Field(..., alias="Enabler 4: Engaging local hire")
    Challenges_2_Skill_Gap: int = Field(..., alias="Challenges 2: Skill Gap ,Retaining resources and workforce Management")
    Enterprise_Age: int = Field(..., description="Age of the enterprise in years")
    Small_Medium_Large: str = Field(..., alias="Small/Medium/Large", description="Size category of the enterprise")
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "Location": 1.0,
                "About Enterprises, Owners Motivation": 3,
                "Enabler 2:Operational Process , Legacy & new machine to balance": 2,
                "Enabler 1: Effortable Digital technologies": 3,
                "Outcome : Growth and Effeciency": 65.5,
                "Enabler 2 :Certification &Standarization": 4,
                "Challanges3: Financial assistant & Incentive ,transparency in institutional support ,": 2,
                "Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges": 3,
                "Enabler 4: Engaging local hire": 2,
                "Challenges 2: Skill Gap ,Retaining resources and workforce Management": 3,
                "Enterprise_Age": 15,
                "Small/Medium/Large": "Medium"
            }
        }


class PredictionResponse(BaseModel):
    """Response model for prediction endpoint"""
    prediction: str
    confidence_scores: Dict[str, float]
    message: str = "Prediction successful"


@router.post("/predict", response_model=PredictionResponse)
async def predict_growth_category(request: PredictionRequest):
    """
    Predict SME growth category based on input features
    
    Returns:
        - prediction: Predicted growth category (High/Medium/Low)
        - confidence_scores: Confidence scores for each category
    """
    try:
        # Get model instance
        model = get_model()
        
        # Convert request to dict with original feature names
        input_data = {
            "Location": request.Location,
            "About Enterprises, Owners Motivation": request.About_Enterprises_Owners_Motivation,
            "Enabler 2:Operational Process , Legacy & new machine to balance": request.Enabler_2_Operational_Process,
            "Enabler 1: Effortable Digital technologies": request.Enabler_1_Effortable_Digital_technologies,
            "Outcome : Growth and Effeciency": request.Outcome_Growth_and_Effeciency,
            "Enabler 2 :Certification &Standarization": request.Enabler_2_Certification_Standarization,
            "Challanges3: Financial assistant & Incentive ,transparency in institutional support ,": request.Challanges3_Financial_assistant,
            "Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges": request.Enabler_3_Administrative_Regulatory,
            "Enabler 4: Engaging local hire": request.Enabler_4_Engaging_local_hire,
            "Challenges 2: Skill Gap ,Retaining resources and workforce Management": request.Challenges_2_Skill_Gap,
            "Enterprise_Age": request.Enterprise_Age,
            "Small/Medium/Large": request.Small_Medium_Large
        }
        
        # Make prediction
        result = model.predict(input_data)
        
        # Save prediction to database (async, don't wait)
        try:
            from threading import Thread
            def save_async():
                try:
                    db = get_database()
                    db.save_prediction(
                        prediction=result['prediction'],
                        confidence_scores=result['confidence_scores'],
                        input_data=input_data
                    )
                except Exception as e:
                    print(f"Warning: Failed to save prediction: {e}")
            
            Thread(target=save_async, daemon=True).start()
        except Exception as db_error:
            print(f"Warning: Failed to start save thread: {db_error}")
        
        return PredictionResponse(
            prediction=result['prediction'],
            confidence_scores=result['confidence_scores']
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@router.get("/model-info")
async def get_model_info():
    """Get model metadata and feature information"""
    try:
        model = get_model()
        info = model.get_model_info()
        return {
            "status": "success",
            "model_info": info
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/features")
async def get_required_features():
    """Get list of all required input features"""
    try:
        model = get_model()
        features = model.get_required_features()
        return {
            "status": "success",
            "features": features
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

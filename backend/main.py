"""
FastAPI Backend for SME Growth Prediction
Main application entry point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import predict, dashboard
import uvicorn
from sklearn.base import BaseEstimator, TransformerMixin


# Define FeatureSelector class globally (required for unpickling)
class FeatureSelector(BaseEstimator, TransformerMixin):
    """Custom transformer for feature selection"""
    def __init__(self, indices):
        self.indices = indices
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X[:, self.indices]

# Create FastAPI app
app = FastAPI(
    title="SME Growth Predictor API",
    description="API for predicting SME growth categories using machine learning",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(predict.router, prefix="/api", tags=["Predictions"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "SME Growth Predictor API",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "health": "/health",
            "predict": "/api/predict",
            "model_info": "/api/model-info",
            "features": "/api/features",
            "docs": "/docs"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "API running"
    }


if __name__ == "__main__":
    print("=" * 80)
    print("SME GROWTH PREDICTOR API")
    print("=" * 80)
    print("\nStarting server...")
    print("API Documentation: http://localhost:8000/docs")
    print("Health Check: http://localhost:8000/health")
    print("\n" + "=" * 80)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

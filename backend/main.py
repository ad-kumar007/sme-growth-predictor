"""
FastAPI Backend for SME Growth Prediction
Main application entry point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import predict, dashboard
import uvicorn
import sys

# Make FeatureSelector available globally for unpickling
# This must be done before any model loading
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureSelector(BaseEstimator, TransformerMixin):
    """Custom transformer for feature selection (required for unpickling)"""
    def __init__(self, indices):
        self.indices = indices
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X[:, self.indices]

# Register FeatureSelector in __main__ module for pickle
sys.modules['__main__'].FeatureSelector = FeatureSelector

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
        "message": "SME Growth Predictor API is running",
        "version": "1.0.0",
        "endpoints": {
            "predict": "/api/predict",
            "model_info": "/api/model-info",
            "dashboard": "/api/dashboard/stats",
            "docs": "/docs"
        }
    }


@app.get("/wake")
async def wake_up():
    """Wake up endpoint to prevent cold starts"""
    return {
        "status": "awake",
        "message": "Server is ready"
    }


if __name__ == "__main__":
    import os
    
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("API_HOST", "0.0.0.0")
    
    print("=" * 80)
    print("SME GROWTH PREDICTOR API")
    print("=" * 80)
    print(f"\nStarting server on {host}:{port}...")
    print(f"API Documentation: http://localhost:{port}/docs")
    print(f"Health Check: http://localhost:{port}/health")
    print("\n" + "=" * 80)
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True
    )

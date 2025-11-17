# 📈 SME Growth Predictor

A full-stack machine learning application that predicts Small and Medium Enterprise (SME) growth categories using advanced ML techniques.

![Tech Stack](https://img.shields.io/badge/React-18.2-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![Python](https://img.shields.io/badge/Python-3.12-yellow)
![ML](https://img.shields.io/badge/ML-scikit--learn-orange)

## 🎯 Overview

This application leverages a trained Random Forest classifier to predict whether an SME will experience **High**, **Medium**, or **Low** growth based on 12 key business and operational metrics.

### Key Features

- ✅ **Real-time Predictions** - Instant growth category predictions with confidence scores
- ✅ **Interactive UI** - Modern, responsive React frontend with Tailwind CSS
- ✅ **RESTful API** - FastAPI backend with automatic documentation
- ✅ **ML Pipeline** - Complete preprocessing and feature selection pipeline
- ✅ **Data Validation** - Robust input validation and error handling
- ✅ **Visual Results** - Interactive charts showing confidence breakdowns

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Test Accuracy | 81% |
| F1 Score (Macro) | 0.76 |
| Train-Test Gap | 15% |
| Features Used | 12 |

## 🏗️ Project Structure

```
sme-growth-predictor/
├── frontend/                 # React frontend
│   ├── src/
│   │   ├── components/      # Reusable React components
│   │   │   └── ResultsModal.jsx
│   │   ├── pages/           # Page components
│   │   │   ├── Home.jsx
│   │   │   ├── PredictionForm.jsx
│   │   │   └── About.jsx
│   │   ├── services/        # API integration
│   │   │   └── api.js
│   │   ├── App.jsx          # Main app component
│   │   ├── main.jsx         # Entry point
│   │   └── index.css        # Global styles
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
├── backend/                  # FastAPI backend
│   ├── routes/              # API routes
│   │   └── predict.py
│   ├── models/              # ML model loader
│   │   └── model_loader.py
│   ├── main.py              # FastAPI app
│   ├── requirements.txt
│   └── .env.example
├── ml_model/                 # Trained ML model
│   └── sme_digitalization_model_final.pkl
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.12+**
- **Node.js 18+** and npm
- **Git**

### 1. Clone the Repository

```bash
cd sme-growth-predictor
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the backend server
python main.py
```

Backend will run on: **http://localhost:8000**

API Documentation: **http://localhost:8000/docs**

### 3. Frontend Setup

Open a new terminal:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will run on: **http://localhost:3000**

## 📝 API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### 1. Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "message": "API running"
}
```

#### 2. Make Prediction
```http
POST /api/predict
```

**Request Body:**
```json
{
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
```

**Response:**
```json
{
  "prediction": "High",
  "confidence_scores": {
    "High": 0.85,
    "Medium": 0.10,
    "Low": 0.05
  },
  "message": "Prediction successful"
}
```

#### 3. Get Model Info
```http
GET /api/model-info
```

**Response:**
```json
{
  "status": "success",
  "model_info": {
    "label_mapping": {"0": "High", "1": "Low", "2": "Medium"},
    "numeric_features": [...],
    "categorical_features": [...],
    "performance": {...},
    "best_params": {...}
  }
}
```

#### 4. Get Required Features
```http
GET /api/features
```

**Response:**
```json
{
  "status": "success",
  "features": {
    "numeric": [...],
    "categorical": [...],
    "all": [...]
  }
}
```

## 🧪 Testing the API

### Using cURL

```bash
curl -X POST "http://localhost:8000/api/predict" \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

### Using Python

```python
import requests

url = "http://localhost:8000/api/predict"
data = {
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

response = requests.post(url, json=data)
print(response.json())
```

## 📦 Building for Production

### Frontend

```bash
cd frontend
npm run build
```

Build output will be in `frontend/dist/`

### Backend

The backend is production-ready. For deployment:

1. Set environment variables
2. Use a production ASGI server (Uvicorn with workers)
3. Configure CORS for your domain

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 🔧 Configuration

### Backend Environment Variables

Create a `.env` file in the `backend/` directory:

```env
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=True
CORS_ORIGINS=http://localhost:3000
MODEL_PATH=../ml_model/sme_digitalization_model_final.pkl
```

### Frontend Environment Variables

Create a `.env` file in the `frontend/` directory:

```env
VITE_API_URL=http://localhost:8000
```

## 📸 Screenshots

### Home Page
Modern landing page with feature highlights and call-to-action.

### Prediction Form
Comprehensive form with all 12 required business metrics, with helpful tooltips and validation.

### Results Modal
Interactive results display with:
- Predicted growth category badge
- Confidence score breakdown
- Visual bar chart
- Actionable insights

### About Page
Detailed information about the dataset, model, and technical stack.

## 🛠️ Technology Stack

### Frontend
- **React 18** - UI framework
- **Tailwind CSS** - Styling
- **React Router** - Navigation
- **Recharts** - Data visualization
- **Axios** - HTTP client
- **Vite** - Build tool

### Backend
- **FastAPI** - Web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **Python 3.12** - Runtime

### Machine Learning
- **scikit-learn** - ML library
- **pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Random Forest** - Classification algorithm

## 📚 Model Details

### Input Features (12 total)

**Numeric Features (11):**
1. Location - Geographic location code
2. About Enterprises, Owners Motivation - Owner motivation level (1-5)
3. Enabler 2: Operational Process - Operational maturity (1-5)
4. Enabler 1: Effortable Digital technologies - Digital tech access (1-5)
5. Outcome: Growth and Efficiency - Current performance score
6. Enabler 2: Certification & Standardization - Certification level (1-5)
7. Challenges 3: Financial assistance - Financial challenges (1-5)
8. Enabler 3: Administrative Hurdles - Regulatory challenges (1-5)
9. Enabler 4: Engaging local hire - Workforce engagement (1-5)
10. Challenges 2: Skill Gap - Workforce challenges (1-5)
11. Enterprise_Age - Age in years

**Categorical Features (1):**
1. Small/Medium/Large - Enterprise size category

### Output
- **Prediction**: One of `High`, `Medium`, or `Low`
- **Confidence Scores**: Probability for each category (sum = 1.0)

### Model Pipeline
1. **Preprocessing**: Median imputation + StandardScaler for numeric, Ordinal encoding for categorical
2. **Feature Selection**: Top 10 features via Mutual Information
3. **Classification**: Random Forest with balanced class weights
4. **Hyperparameters**: Optimized via RandomizedSearchCV with 5-fold CV

## 🐛 Troubleshooting

### Backend Issues

**Model file not found:**
```
Ensure ml_model/sme_digitalization_model_final.pkl exists
```

**Port already in use:**
```bash
# Change port in main.py or use:
uvicorn main:app --port 8001
```

### Frontend Issues

**API connection failed:**
- Verify backend is running on port 8000
- Check CORS configuration
- Verify API_URL in frontend/.env

**Build errors:**
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

## 🚀 Deployment

### Quick Deploy Options

**Docker (Recommended):**
```bash
docker-compose up --build
```

**Cloud Platforms:**
- **Backend**: Deploy to [Render](https://render.com) or [Railway](https://railway.app)
- **Frontend**: Deploy to [Vercel](https://vercel.com) or [Netlify](https://netlify.com)

### Detailed Deployment Guide

See **[DEPLOYMENT.md](./DEPLOYMENT.md)** for complete step-by-step instructions including:
- 🐳 Docker deployment (local & cloud)
- 🎨 Backend deployment on Render
- ⚡ Frontend deployment on Vercel
- 🔄 Alternative platforms (Railway, AWS, Netlify)
- 🔐 Environment variable configuration
- 🐛 Troubleshooting guide

---

## 📄 License

This project is for educational and demonstration purposes.

## 👥 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📧 Support

For questions or issues, please open an issue on the repository.

---

**Built with ❤️ using React, FastAPI, and scikit-learn**

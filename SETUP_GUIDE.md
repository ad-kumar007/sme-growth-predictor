# 🚀 SME Growth Predictor - Complete Setup Guide

This guide will walk you through setting up and running the SME Growth Predictor application from scratch.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.12 or higher** - [Download Python](https://www.python.org/downloads/)
- **Node.js 18 or higher** - [Download Node.js](https://nodejs.org/)
- **npm** (comes with Node.js)
- **Git** (optional, for cloning)

### Verify Installations

```bash
python --version    # Should show 3.12+
node --version      # Should show 18+
npm --version       # Should show 9+
```

## 📁 Project Structure Overview

```
sme-growth-predictor/
├── backend/          # FastAPI Python backend
├── frontend/         # React frontend
├── ml_model/         # Trained ML model (.pkl file)
├── README.md
└── SETUP_GUIDE.md
```

## 🔧 Step-by-Step Setup

### Step 1: Navigate to Project Directory

```bash
cd sme-growth-predictor
```

### Step 2: Backend Setup

#### 2.1 Navigate to Backend

```bash
cd backend
```

#### 2.2 Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

#### 2.3 Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- FastAPI
- Uvicorn
- Pydantic
- pandas
- numpy
- scikit-learn

#### 2.4 Verify Model File

Ensure the model file exists:
```bash
# Windows
dir ..\ml_model\sme_digitalization_model_final.pkl

# Mac/Linux
ls ../ml_model/sme_digitalization_model_final.pkl
```

If the file is missing, you need to place the trained model in `ml_model/` directory.

#### 2.5 Start Backend Server

```bash
python main.py
```

You should see:
```
================================================================================
SME GROWTH PREDICTOR API
================================================================================

Starting server...
API Documentation: http://localhost:8000/docs
Health Check: http://localhost:8000/health

================================================================================
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

✅ **Backend is now running on http://localhost:8000**

Keep this terminal open and running.

### Step 3: Frontend Setup

Open a **NEW terminal window** (keep backend running in the first one).

#### 3.1 Navigate to Frontend

```bash
cd sme-growth-predictor/frontend
```

#### 3.2 Install Node Dependencies

```bash
npm install
```

This will install:
- React
- React Router
- Tailwind CSS
- Axios
- Recharts
- Vite

This may take 2-3 minutes.

#### 3.3 Start Frontend Development Server

```bash
npm run dev
```

You should see:
```
  VITE v5.0.8  ready in 500 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
  ➜  press h to show help
```

✅ **Frontend is now running on http://localhost:3000**

### Step 4: Access the Application

Open your web browser and navigate to:

**http://localhost:3000**

You should see the SME Growth Predictor home page!

## 🧪 Testing the Application

### Test 1: Health Check

Open a new terminal and run:

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "message": "API running"
}
```

### Test 2: API Documentation

Visit: **http://localhost:8000/docs**

You'll see interactive Swagger UI documentation where you can test all API endpoints.

### Test 3: Make a Prediction via UI

1. Go to http://localhost:3000
2. Click "Make Prediction" or "Start Prediction"
3. Fill in all form fields with sample data
4. Click "Predict Growth Category"
5. View the results in the modal popup

### Test 4: Run Automated Tests

From the project root directory:

```bash
cd sme-growth-predictor
python test_api.py
```

This will run a comprehensive test suite covering all API endpoints.

## 🎨 Using the Application

### Home Page
- Overview of the application
- Key features
- Model performance stats
- "How It Works" section

### Prediction Form Page
- Fill in 12 required business metrics
- All fields have helpful tooltips
- Real-time validation
- Submit to get instant predictions

### Results Modal
- Predicted growth category (High/Medium/Low)
- Confidence score breakdown
- Interactive bar chart
- Actionable insights

### About Page
- Dataset information
- Model details and performance
- Technology stack
- Usage instructions

## 🔍 Troubleshooting

### Issue: Backend won't start

**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
cd backend
pip install -r requirements.txt
```

**Error:** `FileNotFoundError: Model file not found`

**Solution:** Ensure `ml_model/sme_digitalization_model_final.pkl` exists in the correct location.

### Issue: Frontend won't start

**Error:** `Cannot find module 'react'`

**Solution:**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

**Error:** `Port 3000 is already in use`

**Solution:** Either:
1. Stop the process using port 3000
2. Or change the port in `vite.config.js`:
```javascript
server: {
  port: 3001  // Change to any available port
}
```

### Issue: API connection failed

**Symptoms:** Frontend shows "An error occurred during prediction"

**Solutions:**
1. Verify backend is running: `curl http://localhost:8000/health`
2. Check browser console for CORS errors
3. Verify `.env` file in frontend has correct API URL
4. Restart both frontend and backend

### Issue: CORS errors

**Error:** `Access to XMLHttpRequest blocked by CORS policy`

**Solution:** In `backend/main.py`, verify CORS middleware includes your frontend URL:
```python
allow_origins=["http://localhost:3000"]
```

## 📦 Building for Production

### Frontend Production Build

```bash
cd frontend
npm run build
```

Build output will be in `frontend/dist/`

To preview the production build:
```bash
npm run preview
```

### Backend Production Deployment

For production, use Uvicorn with multiple workers:

```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 🌐 Deployment Options

### Option 1: Deploy to Vercel (Frontend) + Render (Backend)

**Frontend (Vercel):**
1. Push code to GitHub
2. Connect repository to Vercel
3. Set build command: `npm run build`
4. Set output directory: `dist`
5. Add environment variable: `VITE_API_URL=<your-backend-url>`

**Backend (Render):**
1. Create new Web Service on Render
2. Connect repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Upload model file to persistent storage

### Option 2: Docker Deployment

Create `Dockerfile` for backend:
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Create `Dockerfile` for frontend:
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
CMD ["npm", "run", "preview"]
```

## 📝 Environment Variables Reference

### Backend (.env)
```env
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=True
CORS_ORIGINS=http://localhost:3000
MODEL_PATH=../ml_model/sme_digitalization_model_final.pkl
```

### Frontend (.env)
```env
VITE_API_URL=http://localhost:8000
```

## 🎯 Quick Commands Reference

### Backend
```bash
# Start development server
python main.py

# Start with custom port
uvicorn main:app --port 8001

# Production mode
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Frontend
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📞 Getting Help

If you encounter issues:

1. Check this guide's Troubleshooting section
2. Review the main README.md
3. Check API documentation at http://localhost:8000/docs
4. Review browser console for frontend errors
5. Check terminal output for backend errors

## ✅ Success Checklist

- [ ] Python 3.12+ installed
- [ ] Node.js 18+ installed
- [ ] Backend dependencies installed
- [ ] Frontend dependencies installed
- [ ] Model file in correct location
- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] Health check returns success
- [ ] Can access home page
- [ ] Can submit prediction form
- [ ] Results display correctly

---

**Congratulations! Your SME Growth Predictor is now fully set up and running! 🎉**

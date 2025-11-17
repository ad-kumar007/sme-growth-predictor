# 🚀 Deployment Guide - SME Growth Predictor

Complete guide for deploying the SME Growth Predictor application to various platforms.

## 📋 Table of Contents

1. [Docker Deployment (Local & Cloud)](#docker-deployment)
2. [Backend Deployment on Render](#backend-on-render)
3. [Frontend Deployment on Vercel](#frontend-on-vercel)
4. [Alternative Platforms](#alternative-platforms)
5. [Environment Variables](#environment-variables)
6. [Troubleshooting](#troubleshooting)

---

## 🐳 Docker Deployment

### Prerequisites
- Docker installed ([Download](https://www.docker.com/get-started))
- Docker Compose installed

### Local Deployment with Docker

1. **Clone the repository**
```bash
git clone https://github.com/ad-kumar007/sme-growth-predictor.git
cd sme-growth-predictor
```

2. **Create environment file**
```bash
cp .env.example .env
```

3. **Build and run with Docker Compose**
```bash
docker-compose up --build
```

4. **Access the application**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

5. **Stop the application**
```bash
docker-compose down
```

### Production Docker Deployment

For production on a VPS or cloud VM:

```bash
# Build for production
docker-compose -f docker-compose.yml up -d --build

# View logs
docker-compose logs -f

# Restart services
docker-compose restart

# Stop services
docker-compose down
```

---

## 🎨 Backend Deployment on Render

### Step-by-Step Guide

#### 1. Prepare Your Repository
Ensure your code is pushed to GitHub with the ML model file included.

#### 2. Create Render Account
- Go to [render.com](https://render.com)
- Sign up with GitHub

#### 3. Create New Web Service

**a) From Dashboard:**
- Click "New +" → "Web Service"
- Connect your GitHub repository
- Select `sme-growth-predictor`

**b) Configure Service:**

| Setting | Value |
|---------|-------|
| **Name** | `sme-growth-predictor-api` |
| **Region** | Choose closest to your users |
| **Branch** | `main` |
| **Root Directory** | `backend` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn main:app --host 0.0.0.0 --port $PORT` |
| **Instance Type** | Free or Starter |

**c) Environment Variables:**

Add these in the "Environment" section:

```
MODEL_PATH=/opt/render/project/src/ml_model/sme_digitalization_model_final.pkl
CORS_ORIGINS=https://your-frontend-url.vercel.app
API_HOST=0.0.0.0
API_PORT=10000
```

**d) Advanced Settings:**
- **Auto-Deploy**: Enable (deploys on git push)
- **Health Check Path**: `/health`

#### 4. Deploy
- Click "Create Web Service"
- Wait for deployment (5-10 minutes)
- Note your backend URL: `https://sme-growth-predictor-api.onrender.com`

#### 5. Upload ML Model

Since the model file is large, you have two options:

**Option A: Include in Git (if < 100MB)**
```bash
git lfs track "*.pkl"
git add ml_model/sme_digitalization_model_final.pkl
git commit -m "Add ML model"
git push
```

**Option B: Use Render Disk**
- Go to your service → "Disks"
- Add a disk at `/opt/render/project/src/ml_model`
- Upload model via SFTP or mount script

#### 6. Verify Deployment
```bash
curl https://your-app.onrender.com/health
curl https://your-app.onrender.com/api/model-info
```

---

## ⚡ Frontend Deployment on Vercel

### Step-by-Step Guide

#### 1. Prepare Repository
Ensure frontend code is in the `frontend/` directory.

#### 2. Create Vercel Account
- Go to [vercel.com](https://vercel.com)
- Sign up with GitHub

#### 3. Import Project

**a) From Dashboard:**
- Click "Add New..." → "Project"
- Import `sme-growth-predictor` repository

**b) Configure Project:**

| Setting | Value |
|---------|-------|
| **Framework Preset** | Vite |
| **Root Directory** | `frontend` |
| **Build Command** | `npm run build` |
| **Output Directory** | `dist` |
| **Install Command** | `npm install` |

**c) Environment Variables:**

Add in "Environment Variables" section:

```
VITE_API_BASE_URL=https://sme-growth-predictor-api.onrender.com
```

#### 4. Deploy
- Click "Deploy"
- Wait for build (2-5 minutes)
- Note your frontend URL: `https://sme-growth-predictor.vercel.app`

#### 5. Update Backend CORS

Go back to Render and update the `CORS_ORIGINS` variable:
```
CORS_ORIGINS=https://sme-growth-predictor.vercel.app
```

#### 6. Verify Deployment
- Visit your Vercel URL
- Test the prediction form
- Check browser console for errors

---

## 🔄 Alternative Platforms

### Backend Alternatives

#### Railway
1. Go to [railway.app](https://railway.app)
2. "New Project" → "Deploy from GitHub"
3. Select repository
4. Configure:
   - Root: `backend`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables
6. Deploy

#### AWS EC2
```bash
# SSH into EC2 instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Clone and run
git clone https://github.com/ad-kumar007/sme-growth-predictor.git
cd sme-growth-predictor
docker-compose up -d
```

#### Heroku
```bash
# Install Heroku CLI
heroku login
heroku create sme-growth-predictor-api

# Deploy
git subtree push --prefix backend heroku main

# Set environment variables
heroku config:set MODEL_PATH=/app/ml_model/sme_digitalization_model_final.pkl
```

### Frontend Alternatives

#### Netlify
1. Go to [netlify.com](https://netlify.com)
2. "Add new site" → "Import from Git"
3. Configure:
   - Base directory: `frontend`
   - Build command: `npm run build`
   - Publish directory: `frontend/dist`
4. Add environment variable: `VITE_API_BASE_URL`
5. Deploy

#### GitHub Pages (Static Only)
```bash
cd frontend
npm run build
npx gh-pages -d dist
```

---

## 🔐 Environment Variables

### Development (.env)
```bash
# Backend
API_HOST=0.0.0.0
API_PORT=8000
MODEL_PATH=../ml_model/sme_digitalization_model_final.pkl
CORS_ORIGINS=http://localhost:3000

# Frontend
VITE_API_BASE_URL=http://localhost:8000
```

### Production

**Backend (Render/Railway):**
```bash
MODEL_PATH=/opt/render/project/src/ml_model/sme_digitalization_model_final.pkl
CORS_ORIGINS=https://your-frontend.vercel.app
API_HOST=0.0.0.0
API_PORT=$PORT  # Automatically set by platform
```

**Frontend (Vercel/Netlify):**
```bash
VITE_API_BASE_URL=https://your-backend.onrender.com
```

---

## 🐛 Troubleshooting

### Common Issues

#### 1. CORS Errors
**Problem:** Frontend can't connect to backend

**Solution:**
- Verify `CORS_ORIGINS` in backend includes your frontend URL
- Check browser console for exact error
- Ensure no trailing slashes in URLs

#### 2. Model Not Found
**Problem:** `FileNotFoundError: Model file not found`

**Solution:**
- Verify `MODEL_PATH` environment variable
- Check model file is in repository
- For large files, use Git LFS or disk mount

#### 3. Build Failures

**Backend:**
```bash
# Check Python version
python --version  # Should be 3.11+

# Install dependencies locally
pip install -r requirements.txt
```

**Frontend:**
```bash
# Clear cache and rebuild
rm -rf node_modules dist
npm install
npm run build
```

#### 4. Health Check Failing
**Problem:** Render shows "Service Unhealthy"

**Solution:**
- Check logs: `docker logs sme-backend`
- Verify `/health` endpoint works locally
- Increase health check timeout in Render settings

#### 5. Slow Predictions
**Problem:** First prediction takes too long

**Solution:**
- Use paid tier for better performance
- Implement model caching (already done)
- Consider serverless functions for sporadic use

---

## 📊 Monitoring & Logs

### View Logs

**Docker:**
```bash
docker-compose logs -f backend
docker-compose logs -f frontend
```

**Render:**
- Dashboard → Your Service → "Logs" tab
- Real-time log streaming

**Vercel:**
- Dashboard → Your Project → "Deployments" → Click deployment → "Logs"

### Health Checks

**Backend:**
```bash
curl https://your-backend-url.onrender.com/health
```

**Frontend:**
```bash
curl https://your-frontend-url.vercel.app
```

---

## 🎯 Production Checklist

Before going live:

- [ ] Environment variables configured
- [ ] CORS origins updated
- [ ] ML model uploaded and accessible
- [ ] Health checks passing
- [ ] SSL/HTTPS enabled (automatic on Vercel/Render)
- [ ] Error logging configured
- [ ] Database backups enabled (if using persistent storage)
- [ ] Performance tested with sample predictions
- [ ] Documentation updated with live URLs

---

## 📞 Support

For deployment issues:
- Check [Render Docs](https://render.com/docs)
- Check [Vercel Docs](https://vercel.com/docs)
- Review application logs
- Open GitHub issue

---

## 🚀 Quick Deploy Commands

**Local Docker:**
```bash
docker-compose up --build
```

**Render (via CLI):**
```bash
render deploy
```

**Vercel (via CLI):**
```bash
npm i -g vercel
cd frontend
vercel --prod
```

---

**Deployment complete! Your ML application is now live! 🎉**

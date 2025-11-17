# ⚡ Quick Start Guide - SME Growth Predictor

Get up and running in 5 minutes!

## 🎯 Prerequisites

- Python 3.12+
- Node.js 18+
- npm

## 🚀 Quick Setup

### Step 1: Install Backend Dependencies (2 minutes)

```bash
cd sme-growth-predictor/backend
pip install -r requirements.txt
```

### Step 2: Install Frontend Dependencies (2 minutes)

```bash
cd ../frontend
npm install
```

### Step 3: Start Backend (Terminal 1)

```bash
cd ../backend
python main.py
```

✅ Backend running at: **http://localhost:8000**

### Step 4: Start Frontend (Terminal 2 - New Window)

```bash
cd ../frontend
npm run dev
```

✅ Frontend running at: **http://localhost:3000**

## 🎉 You're Ready!

Open your browser and go to: **http://localhost:3000**

## 🧪 Quick Test

### Test the API:

```bash
curl http://localhost:8000/health
```

Expected: `{"status":"healthy","message":"API running"}`

### Test a Prediction:

1. Go to http://localhost:3000
2. Click "Make Prediction"
3. Fill the form with sample data:
   - Location: `1.0`
   - Owner Motivation: `3`
   - Operational Process: `2`
   - Digital Technologies: `3`
   - Growth & Efficiency: `65.5`
   - Certification: `4`
   - Financial Challenges: `2`
   - Administrative Hurdles: `3`
   - Local Hiring: `2`
   - Skill Gap: `3`
   - Enterprise Age: `15`
   - Size: `Medium`
4. Click "Predict Growth Category"
5. View results!

## 📚 Next Steps

- Read [README.md](README.md) for detailed documentation
- Check [SETUP_GUIDE.md](SETUP_GUIDE.md) for troubleshooting
- View API docs at http://localhost:8000/docs
- Run tests: `python test_api.py`

## 🔥 Quick Commands

### Backend
```bash
# Start server
python main.py

# Run tests
python ../test_api.py
```

### Frontend
```bash
# Start dev server
npm run dev

# Build for production
npm run build
```

## ⚠️ Common Issues

**Backend won't start?**
```bash
pip install -r requirements.txt
```

**Frontend won't start?**
```bash
npm install
```

**Port already in use?**
- Kill process on port 8000 (backend) or 3000 (frontend)
- Or change port in config files

---

**That's it! You're all set! 🎊**

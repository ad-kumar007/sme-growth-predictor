# 📋 Deployment Checklist

Use this checklist to ensure smooth deployment of the SME Growth Predictor application.

## Pre-Deployment

### Code Preparation
- [ ] All code committed and pushed to GitHub
- [ ] ML model file (`sme_digitalization_model_final.pkl`) is in repository
- [ ] `.gitignore` properly configured
- [ ] No sensitive data in code (API keys, passwords, etc.)
- [ ] All dependencies listed in `requirements.txt` and `package.json`

### Testing
- [ ] Application runs locally without errors
- [ ] All API endpoints tested
- [ ] Frontend connects to backend successfully
- [ ] Predictions working correctly
- [ ] Dashboard displaying data
- [ ] PDF reports generating

### Documentation
- [ ] README.md updated with deployment info
- [ ] DEPLOYMENT.md reviewed
- [ ] Environment variables documented
- [ ] API documentation accessible

---

## Docker Deployment

### Local Testing
- [ ] Docker and Docker Compose installed
- [ ] `.env` file created from `.env.example`
- [ ] `docker-compose up --build` runs successfully
- [ ] Both services healthy
- [ ] Can access frontend at localhost:3000
- [ ] Can access backend at localhost:8000
- [ ] API docs accessible at localhost:8000/docs

### Production Docker
- [ ] Production environment variables configured
- [ ] Volumes mounted correctly
- [ ] Health checks passing
- [ ] Logs configured
- [ ] Restart policies set

---

## Backend Deployment (Render)

### Account Setup
- [ ] Render account created
- [ ] GitHub connected to Render
- [ ] Payment method added (if using paid tier)

### Service Configuration
- [ ] New Web Service created
- [ ] Repository connected
- [ ] Root directory set to `backend`
- [ ] Python runtime selected
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Environment Variables
- [ ] `MODEL_PATH` set correctly
- [ ] `CORS_ORIGINS` includes frontend URL
- [ ] `API_HOST` set to `0.0.0.0`
- [ ] All required variables added

### Model Upload
- [ ] ML model accessible to service
- [ ] Model path verified
- [ ] Model loads successfully

### Verification
- [ ] Service deployed successfully
- [ ] Health check endpoint responding
- [ ] `/api/model-info` returns data
- [ ] Can make test prediction
- [ ] Logs show no errors
- [ ] Note backend URL for frontend config

---

## Frontend Deployment (Vercel)

### Account Setup
- [ ] Vercel account created
- [ ] GitHub connected to Vercel

### Project Configuration
- [ ] Project imported from GitHub
- [ ] Framework preset: Vite
- [ ] Root directory: `frontend`
- [ ] Build command: `npm run build`
- [ ] Output directory: `dist`

### Environment Variables
- [ ] `VITE_API_BASE_URL` set to backend URL
- [ ] All environment variables added

### Build & Deploy
- [ ] Initial deployment successful
- [ ] Build logs checked for errors
- [ ] No build warnings

### Verification
- [ ] Frontend accessible at Vercel URL
- [ ] All pages load correctly
- [ ] Can navigate between pages
- [ ] Prediction form displays
- [ ] Dashboard loads
- [ ] About page shows correctly

---

## Integration Testing

### CORS Configuration
- [ ] Backend CORS updated with frontend URL
- [ ] Backend redeployed with new CORS settings
- [ ] No CORS errors in browser console

### End-to-End Testing
- [ ] Can submit prediction from deployed frontend
- [ ] Prediction returns successfully
- [ ] Results modal displays
- [ ] Confidence scores shown
- [ ] Dashboard updates with new prediction
- [ ] Can download PDF report
- [ ] All charts render correctly

### Performance
- [ ] First prediction completes in reasonable time
- [ ] Subsequent predictions are fast
- [ ] No timeout errors
- [ ] Images and assets load quickly

---

## Post-Deployment

### Monitoring
- [ ] Health check endpoints configured
- [ ] Error logging enabled
- [ ] Performance monitoring set up
- [ ] Uptime monitoring configured

### Documentation
- [ ] README updated with live URLs
- [ ] Deployment guide reflects actual setup
- [ ] Environment variables documented
- [ ] Known issues documented

### Security
- [ ] HTTPS enabled (automatic on Vercel/Render)
- [ ] Environment variables secured
- [ ] No sensitive data exposed
- [ ] CORS properly configured
- [ ] API rate limiting considered

### Backup
- [ ] Database backup strategy (if applicable)
- [ ] Model file backed up
- [ ] Code repository backed up

---

## Troubleshooting Checklist

If something doesn't work:

### Backend Issues
- [ ] Check Render logs
- [ ] Verify environment variables
- [ ] Test health endpoint
- [ ] Verify model path
- [ ] Check Python version compatibility
- [ ] Review CORS configuration

### Frontend Issues
- [ ] Check Vercel deployment logs
- [ ] Verify build completed successfully
- [ ] Check browser console for errors
- [ ] Verify API URL in environment variables
- [ ] Test API connection directly
- [ ] Clear browser cache

### Connection Issues
- [ ] Verify backend URL in frontend config
- [ ] Check CORS settings
- [ ] Test API endpoints with curl/Postman
- [ ] Verify no firewall blocking
- [ ] Check SSL certificate (should be automatic)

---

## Rollback Plan

If deployment fails:

1. **Immediate Actions**
   - [ ] Revert to previous working deployment
   - [ ] Check error logs
   - [ ] Notify users if necessary

2. **Investigation**
   - [ ] Identify what changed
   - [ ] Review deployment logs
   - [ ] Test locally

3. **Fix & Redeploy**
   - [ ] Fix identified issues
   - [ ] Test thoroughly locally
   - [ ] Deploy to staging (if available)
   - [ ] Deploy to production

---

## Success Criteria

Deployment is successful when:

- ✅ Frontend accessible at public URL
- ✅ Backend accessible and responding
- ✅ Can make predictions end-to-end
- ✅ Dashboard shows statistics
- ✅ PDF reports download correctly
- ✅ No console errors
- ✅ Performance acceptable
- ✅ Health checks passing
- ✅ Documentation updated

---

## Maintenance Schedule

### Daily
- [ ] Check error logs
- [ ] Monitor uptime
- [ ] Review performance metrics

### Weekly
- [ ] Review usage statistics
- [ ] Check for security updates
- [ ] Backup database

### Monthly
- [ ] Update dependencies
- [ ] Review and optimize performance
- [ ] Update documentation

---

**Deployment Date:** _____________

**Deployed By:** _____________

**Backend URL:** _____________

**Frontend URL:** _____________

**Notes:** _____________

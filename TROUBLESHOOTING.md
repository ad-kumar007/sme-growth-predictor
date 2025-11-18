# 🔧 Troubleshooting Guide

## Common Issues and Solutions

### 🚨 Dashboard Shows "Retry" Error

**Symptoms:**
- Dashboard loads on one laptop but not another
- Shows "Connection Error" or "Failed to load dashboard data"
- Works for you but not for others

**Causes & Solutions:**

#### 1. **Backend Server is Sleeping (Most Common)**

**Cause:** Render free tier puts inactive services to sleep after 15 minutes of inactivity.

**Solution:**
- **Wait 30-60 seconds** after clicking Retry
- The first request wakes up the server
- Subsequent requests will be fast

**How to check:**
1. Visit: https://sme-growth-predictor-1.onrender.com/health
2. If it takes 30+ seconds to load, the server was asleep
3. After it loads, refresh your dashboard

#### 2. **CORS / Network Issues**

**Cause:** Browser blocking cross-origin requests or network firewall.

**Solution:**
- Open browser console (F12)
- Look for CORS errors
- Check if requests are being blocked
- Try a different network/browser

**Quick test:**
```bash
# Test backend directly
curl https://sme-growth-predictor-1.onrender.com/health
```

#### 3. **Wrong API URL in Frontend**

**Cause:** Frontend is pointing to wrong backend URL.

**Check Vercel Environment Variables:**
1. Go to Vercel Dashboard
2. Your Project → Settings → Environment Variables
3. Verify: `VITE_API_BASE_URL=https://sme-growth-predictor-1.onrender.com`
4. If wrong, update and redeploy

#### 4. **Browser Cache**

**Solution:**
- Hard refresh: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
- Clear browser cache
- Try incognito/private mode

---

## 🔍 Debugging Steps

### Step 1: Check Backend Status

Visit: https://sme-growth-predictor-1.onrender.com/health

**Expected Response:**
```json
{
  "status": "healthy",
  "message": "SME Growth Predictor API is running"
}
```

**If it fails:**
- Backend is down
- Check Render dashboard for errors
- Check Render logs

### Step 2: Check Frontend Console

1. Open browser DevTools (F12)
2. Go to Console tab
3. Look for errors

**Common errors:**

**Error:** `Failed to fetch`
- **Cause:** Backend is sleeping or down
- **Fix:** Wait and retry

**Error:** `CORS policy`
- **Cause:** CORS misconfiguration
- **Fix:** Check backend CORS settings

**Error:** `net::ERR_CONNECTION_REFUSED`
- **Cause:** Backend URL is wrong
- **Fix:** Check environment variables

### Step 3: Check Network Tab

1. Open DevTools → Network tab
2. Refresh page
3. Look for failed requests (red)
4. Click on failed request
5. Check:
   - Request URL (should be your Render URL)
   - Status code
   - Response

---

## ⚡ Quick Fixes

### Fix 1: Wake Up the Backend

**Option A: Visit Health Endpoint**
```
https://sme-growth-predictor-1.onrender.com/health
```

**Option B: Use Wake Endpoint**
```
https://sme-growth-predictor-1.onrender.com/wake
```

**Option C: Make a Prediction**
- Go to "Make Prediction" page
- Submit a prediction
- This wakes up the backend

### Fix 2: Force Redeploy

**Vercel (Frontend):**
```bash
# From your project directory
vercel --prod
```

**Render (Backend):**
- Go to Render Dashboard
- Click "Manual Deploy" → "Deploy latest commit"

### Fix 3: Check Environment Variables

**Vercel:**
```bash
# List environment variables
vercel env ls

# Pull environment variables
vercel env pull
```

**Render:**
- Dashboard → Your Service → Environment
- Verify all variables are set correctly

---

## 🌐 Network Issues

### Corporate/School Network

**Problem:** Firewall blocking external APIs

**Solution:**
- Try on mobile data / personal hotspot
- Ask IT to whitelist:
  - `*.onrender.com`
  - `*.vercel.app`

### VPN Issues

**Problem:** VPN blocking requests

**Solution:**
- Temporarily disable VPN
- Try different VPN server
- Whitelist domains in VPN settings

---

## 📊 Performance Issues

### Slow First Load

**Normal Behavior:**
- First request: 30-60 seconds (cold start)
- Subsequent requests: <2 seconds

**If always slow:**
- Upgrade Render plan (paid tier = no sleep)
- Use keep-alive service (ping every 10 minutes)

### Predictions Taking Too Long

**Check:**
1. Model loaded correctly
2. Database not locked
3. Render logs for errors

**Solution:**
```bash
# Check Render logs
# Dashboard → Your Service → Logs
```

---

## 🔐 CORS Errors

### Symptoms
```
Access to fetch at 'https://...' from origin 'https://...' 
has been blocked by CORS policy
```

### Solution

**Backend (main.py):**
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**Verify CORS is set:**
```bash
curl -H "Origin: https://your-frontend.vercel.app" \
     -H "Access-Control-Request-Method: GET" \
     -X OPTIONS \
     https://sme-growth-predictor-1.onrender.com/health -v
```

---

## 📱 Mobile Issues

### Dashboard Not Loading on Mobile

**Check:**
1. Mobile data vs WiFi
2. Browser compatibility
3. Console errors (use remote debugging)

**Solution:**
- Try different browser
- Clear mobile browser cache
- Check if backend is accessible from mobile network

---

## 🆘 Still Not Working?

### Collect Debug Info

1. **Backend Status:**
   ```
   https://sme-growth-predictor-1.onrender.com/health
   ```

2. **Frontend Console Errors:**
   - Screenshot of browser console (F12)

3. **Network Tab:**
   - Screenshot of failed requests

4. **Environment:**
   - Browser version
   - Operating system
   - Network type (WiFi, mobile, corporate)

### Contact Support

- Open GitHub issue with debug info
- Include screenshots
- Describe exact steps to reproduce

---

## ✅ Verification Checklist

Before reporting an issue, verify:

- [ ] Backend health endpoint responds
- [ ] Frontend environment variables are correct
- [ ] Browser console shows no CORS errors
- [ ] Tried hard refresh (Ctrl+Shift+R)
- [ ] Waited 60 seconds for cold start
- [ ] Tried different browser
- [ ] Tried different network
- [ ] Checked Render logs for errors
- [ ] Checked Vercel deployment logs

---

## 🎯 Prevention

### Keep Backend Awake

**Option 1: Cron Job (Recommended)**
```bash
# Use cron-job.org or similar
# Ping every 10 minutes:
GET https://sme-growth-predictor-1.onrender.com/wake
```

**Option 2: UptimeRobot**
- Free monitoring service
- Pings your backend every 5 minutes
- Prevents sleep

**Option 3: Upgrade to Paid Tier**
- Render Starter plan: $7/month
- No cold starts
- Always-on service

---

## 📞 Quick Links

- **Backend Health:** https://sme-growth-predictor-1.onrender.com/health
- **API Docs:** https://sme-growth-predictor-1.onrender.com/docs
- **Render Dashboard:** https://dashboard.render.com
- **Vercel Dashboard:** https://vercel.com/dashboard
- **GitHub Repo:** https://github.com/ad-kumar007/sme-growth-predictor

---

**Last Updated:** November 2024

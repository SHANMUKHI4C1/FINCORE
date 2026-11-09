# Dependency Installation Guide - FinCore Analytics

**System:** Windows with Python 3.13.2  
**Date:** October 26, 2026

---

## Current Status Summary

✓ **Installed:**
- Python 3.13.2
- pip 25.0.1
- NumPy 2.2.3
- Pandas 2.2.3
- Flask 3.1.2
- PyMongo 4.16.0
- python-dotenv

✗ **Missing Critical:**
- Node.js & npm
- MongoDB
- Flask-CORS
- scikit-learn
- joblib
- reportlab

---

## Installation Commands (Copy & Execute)

### 1. Create Virtual Environment (RECOMMENDED)

```powershell
# Navigate to backend directory
cd "C:\Users\Chinni\Downloads\fintech-core-main\fintech-core-main\backend"

# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\activate

# Verify activation (should see (venv) in prompt)
python --version
```

---

### 2. Install Missing Python Packages

**Option A: Install individually (RECOMMENDED for Python 3.13.2)**

```powershell
# Ensure venv is activated first!

# Core web framework packages
pip install Flask-CORS==4.0.0

# Machine Learning (using versions compatible with Python 3.13.2)
pip install scikit-learn==1.5.2
pip install joblib==1.4.2

# Reports
pip install reportlab==4.2.5

# SMS (optional for Phase 1, but install for completeness)
pip install twilio==9.3.7

# Testing
pip install pytest==8.3.4
pip install pytest-flask==1.3.0

# Date utilities
pip install python-dateutil==2.9.0

# Matplotlib for analytics visualization
pip install matplotlib==3.9.3

# SciPy for advanced analytics
pip install scipy==1.14.1
```

**Option B: Update and use requirements.txt**

First, update requirements.txt versions for Python 3.13 compatibility, then:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

**Verification:**
```powershell
python ../check_packages.py
```

Expected output: All packages show ✓ INSTALLED

---

### 3. Install MongoDB

**Option A: Local MongoDB (RECOMMENDED for development)**

1. **Download:**
   - Visit: https://www.mongodb.com/try/download/community
   - Select: Windows, Current version (7.x)
   - Download MSI installer

2. **Install:**
   - Run installer
   - Choose "Complete" installation
   - Install MongoDB as a Service (check this option)
   - Install MongoDB Compass (GUI tool - optional but helpful)

3. **Verify Installation:**
```powershell
# Check MongoDB service
Get-Service MongoDB

# Should show "Running" status

# Test connection
mongosh
# If successful, you'll see MongoDB shell prompt
# Type: exit
```

4. **Create Data Directory:**
```powershell
# Create data directory if not exists
mkdir C:\data\db
```

**Option B: MongoDB Atlas (Cloud - FREE tier)**

1. Visit: https://www.mongodb.com/cloud/atlas/register
2. Create free account
3. Create free cluster (M0)
4. Get connection string
5. Update `.env` file:
```
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
```

---

### 4. Install Node.js

1. **Download:**
   - Visit: https://nodejs.org/
   - Download LTS version (recommended: 20.x or 22.x)

2. **Install:**
   - Run installer
   - Accept defaults
   - Restart PowerShell after installation

3. **Verify:**
```powershell
node --version
npm --version
```

Expected output:
```
v20.x.x (or v22.x.x)
10.x.x
```

---

### 5. Install Frontend Dependencies

```powershell
# Navigate to frontend directory
cd "C:\Users\Chinni\Downloads\fintech-core-main\fintech-core-main\frontend"

# Install all packages
npm install

# This will install:
# - React 18.2.0
# - React Router 6.20.1
# - Axios 1.6.2
# - Recharts 2.10.3
# - Tailwind CSS 3.4.0
# - Vite 5.0.8
# - and all dev dependencies

# Verification
npm list --depth=0
```

Expected: All packages installed, 0 vulnerabilities reported

---

## Post-Installation Verification

### Test Backend

```powershell
cd backend
.\venv\Scripts\activate
python app.py
```

Expected output:
```
INFO:__main__:Starting Flask application on port 5000
INFO:__main__:Environment: development
INFO:utils.db_connection:Successfully connected to MongoDB
 * Running on http://0.0.0.0:5000
```

**Test health endpoint:**
Open browser: http://localhost:5000/api/health

### Test Frontend

```powershell
cd frontend
npm run dev
```

Expected output:
```
VITE v5.0.8  ready in XXX ms
➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
```

**Test frontend:**
Open browser: http://localhost:5173

---

## Troubleshooting

### Python Packages Fail to Install

**Issue:** Compilation errors with C extensions
**Solution:**
```powershell
# Install Microsoft C++ Build Tools
# Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
# Or use pre-compiled wheels:
pip install --only-binary :all: scikit-learn
```

### MongoDB Won't Start

**Issue:** Service fails to start
**Solution:**
```powershell
# Create data directory
mkdir C:\data\db

# Start manually
mongod --dbpath C:\data\db

# Or check service
sc query MongoDB
net start MongoDB
```

### Node.js Not Recognized

**Issue:** Command not found after installation
**Solution:**
- Restart PowerShell (close and reopen)
- Check PATH environment variable includes Node.js
- Reinstall Node.js with "Add to PATH" checked

### npm install Slow or Hanging

**Issue:** Package installation taking too long
**Solution:**
```powershell
# Clear npm cache
npm cache clean --force

# Try again
npm install
```

### Port Already in Use

**Issue:** Flask or Vite can't start on port
**Solution:**
```powershell
# Check what's using port 5000
netstat -ano | findstr :5000

# Kill the process
taskkill /PID <PID> /F

# Or change port in .env (Flask) or vite.config.js (Frontend)
```

---

## Compatible Version Matrix

| Package | Python 3.13.2 Compatible | Recommended Version |
|---------|--------------------------|---------------------|
| Flask | ✓ Yes | 3.0.0+ |
| Flask-CORS | ✓ Yes | 4.0.0+ |
| NumPy | ✓ Yes | 2.0.0+ |
| Pandas | ✓ Yes | 2.2.0+ |
| scikit-learn | ✓ Yes | 1.5.0+ |
| joblib | ✓ Yes | 1.4.0+ |
| PyMongo | ✓ Yes | 4.6.0+ |
| ReportLab | ✓ Yes | 4.2.0+ |
| Matplotlib | ✓ Yes | 3.9.0+ |
| SciPy | ✓ Yes | 1.14.0+ |

---

## Estimated Installation Time

- Virtual environment: 30 seconds
- Python packages: 5-10 minutes
- MongoDB (local): 10-15 minutes
- Node.js: 5 minutes
- Frontend packages: 3-5 minutes

**Total: 25-40 minutes**

---

## Success Criteria

After completing all installations, verify:

- [ ] Virtual environment activates successfully
- [ ] `python check_packages.py` shows all packages installed
- [ ] MongoDB service is running
- [ ] `mongosh` connects successfully
- [ ] `node --version` and `npm --version` work
- [ ] Frontend `node_modules` directory exists
- [ ] Flask server starts without errors
- [ ] Health endpoint returns JSON
- [ ] Frontend dev server starts
- [ ] Frontend loads in browser

---

**Next Step After Installation:** Run full runtime verification


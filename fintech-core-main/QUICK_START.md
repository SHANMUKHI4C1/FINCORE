# Quick Start Guide

## Phase 1: Foundation & Setup - COMPLETE ✅

### Installation (First Time Only)

#### 1. Backend Setup
```powershell
# Open PowerShell in project root
cd "c:\Users\GSPD\OneDrive\Desktop\fincore analytics\backend"

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify setup
python verify_setup.py
```

#### 2. Frontend Setup
```powershell
# Open NEW PowerShell window
cd "c:\Users\GSPD\OneDrive\Desktop\fincore analytics\frontend"

# Install dependencies (takes 2-3 minutes)
npm install
```

#### 3. MongoDB Setup
```powershell
# Option A: Local MongoDB
# Open NEW PowerShell window
mongod --dbpath C:\data\db

# Option B: MongoDB Atlas
# Edit backend\.env and set MONGODB_URI to your Atlas connection string
```

---

### Running the Application (Every Time)

#### Terminal 1: MongoDB (if using local)
```powershell
mongod --dbpath C:\data\db
```

#### Terminal 2: Backend
```powershell
cd "c:\Users\GSPD\OneDrive\Desktop\fincore analytics\backend"
.\venv\Scripts\activate
python app.py
```
**Wait for:** "Running on http://0.0.0.0:5000"

#### Terminal 3: Frontend
```powershell
cd "c:\Users\GSPD\OneDrive\Desktop\fincore analytics\frontend"
npm run dev
```
**Wait for:** "Local: http://localhost:5173/"

#### Open Browser
- Frontend: http://localhost:5173
- Backend API: http://localhost:5000/api/health

---

### Quick Verification

```powershell
# Test backend health
curl http://localhost:5000/api/health

# Should return JSON with status: "healthy"
```

---

### Troubleshooting

**MongoDB won't start?**
- Create directory: `mkdir C:\data\db`
- Check if already running: `netstat -an | findstr "27017"`

**Port 5000 busy?**
- Change in backend\.env: `FLASK_PORT=5001`
- Restart backend

**npm install fails?**
- Clear cache: `npm cache clean --force`
- Delete node_modules and try again

**Python import errors?**
- Ensure venv is activated (should see `(venv)` in prompt)
- Reinstall: `pip install -r requirements.txt`

---

### Next Phase

When Phase 1 is verified and working, say:
```
Start Phase 2
```

This will implement Income and Expense management (CRUD operations).

---

### Project Structure

```
fincore analytics/
├── backend/          # Flask API (Port 5000)
├── frontend/         # React App (Port 5173)
├── PROJECT_ARCHITECTURE.md
├── DEVELOPMENT_PLAN.md
├── MODULE_DEPENDENCIES.md
└── PHASE1_COMPLETE.md
```

---

### Useful Commands

```powershell
# Backend
cd backend
.\venv\Scripts\activate          # Activate venv
python app.py                    # Run server
python verify_setup.py           # Verify installation
pip list                         # Show installed packages

# Frontend
cd frontend
npm run dev                      # Run dev server
npm run build                    # Build for production
npm run preview                  # Preview production build

# MongoDB
mongosh                          # MongoDB shell
show dbs                         # List databases
use finance_advisor              # Select database
show collections                 # List collections
```

---

**Status:** Phase 1 Complete ✅  
**Next:** Phase 2 - Income & Expense CRUD  
**Progress:** 11% (1/9 phases)

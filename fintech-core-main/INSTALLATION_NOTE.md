# Installation Note

## Issue with Python 3.13

You have Python 3.13, which is very new. Some data science packages (pandas, numpy, scikit-learn) are still building compatibility for it, which causes installation to be very slow (compiling from source).

## Solution Options

### Option 1: Install Python 3.11 (Recommended)
Download and install Python 3.11 from https://www.python.org/downloads/
Then recreate the virtual environment with Python 3.11.

### Option 2: Install Dependencies Manually (Faster for Now)
For Phase 1, we only need basic dependencies. Install these manually:

```powershell
cd "c:\Users\GSPD\OneDrive\Desktop\fincore analytics\backend"
.\venv\Scripts\activate
pip install Flask Flask-CORS pymongo python-dotenv
```

We'll add ML packages (pandas, numpy, scikit-learn) in Phase 3 when you actually need them.

### Option 3: Use requirements_minimal.txt (Phase 1 Only)
```powershell
cd "c:\Users\GSPD\OneDrive\Desktop\fincore analytics\backend"
.\venv\Scripts\activate
pip install -r requirements_minimal.txt
```

## Current Status
- ✅ Backend structure created
- ✅ Frontend structure created  
- ⏳ Python packages need manual installation (see above options)
- ⏳ Frontend packages (npm install) - ready to run

## Next Steps

1. **Install backend dependencies** using one of the options above
2. **Install frontend dependencies:**
   ```powershell
   cd "c:\Users\GSPD\OneDrive\Desktop\fincore analytics\frontend"
   npm install
   ```
3. **Start MongoDB** (if using local)
4. **Run the servers** and test

---

**Note:** The full requirements.txt will work, it just takes 10-15 minutes to install on Python 3.13 because packages are building from source. For faster setup today, use Option 2 or 3.

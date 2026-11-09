# Test MongoDB Atlas Connection

**Purpose:** Verify MongoDB Atlas is properly configured before starting Flask app

---

## Prerequisites

Before testing, ensure:

1. ✅ MongoDB Atlas cluster created
2. ✅ Database user created with password
3. ✅ IP address whitelisted in Network Access
4. ✅ Connection string copied from Atlas
5. ✅ `.env` file updated with your connection string

If you haven't completed these steps, see `MONGODB_ATLAS_SETUP.md`.

---

## Method 1: Using Test Script (RECOMMENDED)

### Run the Test Script

```powershell
# Navigate to backend directory
cd "C:\Users\Chinni\Downloads\fintech-core-main\fintech-core-main\backend"

# Run test script
python test_mongodb_atlas.py
```

### Expected Output (Success)

```
============================================================
MongoDB Atlas Connection Test
============================================================

Database Name: finance_advisor
Connection Type: MongoDB Atlas
Cluster: cluster0.abc123.mongodb.net

Testing connection...

Step 1/4: Attempting connection...
✓ Connection successful

Step 2/4: Accessing database...
✓ Database 'finance_advisor' accessible

Step 3/4: Checking collections...
✓ No collections yet (will be created on first write)

Step 4/4: Testing write permission...
✓ Write permission confirmed
✓ Test document cleaned up

============================================================
✅ ALL TESTS PASSED
============================================================

MongoDB Atlas is properly configured!
You can now start the Flask application.
```

### Possible Failures

#### Connection Timeout

```
❌ FAIL: Connection timeout

Possible causes:
1. IP address not whitelisted in Atlas Network Access
2. Firewall blocking outbound connections
3. Internet connectivity issues
4. Incorrect cluster hostname
```

**Solution:**
1. Go to Atlas → Network Access
2. Click "Add IP Address"
3. Add your current IP or `0.0.0.0/0`
4. Wait 1-2 minutes
5. Test again

#### Authentication Failed

```
❌ FAIL: Authentication error

Possible causes:
1. Incorrect username or password in connection string
2. Database user not created in Atlas
3. Special characters not URL-encoded in password
```

**Solution:**
1. Check database username in `.env` matches Atlas user
2. Verify password is correct (case-sensitive)
3. URL-encode special characters (see CONFIGURE_ENV_FILE.md)
4. Or create new database user with simpler password

---

## Method 2: Using Python Interactive

### Quick Connection Test

```powershell
python
```

```python
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv('MONGODB_URI')

# Test connection
client = MongoClient(uri, serverSelectionTimeoutMS=5000)
client.admin.command('ping')
print("✓ Connected!")

# Show database
db = client['finance_advisor']
print(f"Database: {db.name}")

# Clean up
client.close()
exit()
```

**Expected:** No errors, prints "✓ Connected!"

---

## Method 3: Using MongoDB Compass (GUI)

### Install Compass

1. Download: https://www.mongodb.com/try/download/compass
2. Install and open

### Connect Using Connection String

1. Click "New Connection"
2. Paste your FULL connection string from `.env`:
   ```
   mongodb+srv://USERNAME:PASSWORD@CLUSTER.mongodb.net/?retryWrites=true&w=majority
   ```
3. Click "Connect"
4. You should see:
   - `admin` database
   - `local` database
   - `finance_advisor` database (once created)

---

## Method 4: Start Flask App (Full Test)

### Start the Application

```powershell
# Navigate to backend
cd backend

# Run Flask app
python app.py
```

### Expected Output (Success)

```
INFO:__main__:Starting Flask application on port 5000
INFO:__main__:Environment: development
INFO:__main__:Debug mode: True
INFO:__main__:Database: finance_advisor
INFO:utils.db_connection:Connecting to MongoDB at mongodb+srv://...
INFO:utils.db_connection:Successfully connected to MongoDB database: finance_advisor
INFO:utils.db_connection:Created indexes for 'income' collection
INFO:utils.db_connection:Created indexes for 'expenses' collection
INFO:utils.db_connection:Created indexes for 'budgets' collection
INFO:utils.db_connection:Created indexes for 'ml_models' collection
INFO:utils.db_connection:Created indexes for 'alerts' collection
INFO:utils.db_connection:Initialized 'settings' collection
INFO:utils.db_connection:Database setup completed successfully
INFO:utils.db_connection:MongoDB connection is healthy
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://YOUR_IP:5000
Press CTRL+C to quit
```

### Test Health Endpoint

Open browser or use curl:
```
http://localhost:5000/api/health
```

**Expected JSON response:**
```json
{
  "status": "healthy",
  "message": "AI-Based Personal Finance Advisor API is running",
  "database": {
    "connected": true,
    "message": "MongoDB connection is healthy"
  },
  "features": {
    "analytics_enabled": true,
    "sms_enabled": false,
    "rag_enabled": false
  }
}
```

---

## Verification Checklist

After successful connection:

- [ ] Test script shows "ALL TESTS PASSED"
- [ ] Flask app starts without errors
- [ ] Health endpoint shows `"connected": true`
- [ ] MongoDB Compass can connect (optional)
- [ ] Collections are created in Atlas dashboard

---

## Troubleshooting Common Issues

### pymongo not installed

```
ModuleNotFoundError: No module named 'pymongo'
```

**Solution:**
```powershell
pip install pymongo python-dotenv
```

### .env file not found

```
❌ FAIL: MONGODB_URI not set in .env file
```

**Solution:**
1. Ensure `.env` exists in `backend/` directory
2. Copy from `.env.example` if needed
3. Add your MongoDB URI

### Connection works but Flask fails

**Possible cause:** Import errors or missing packages

**Solution:**
```powershell
pip install Flask Flask-CORS pymongo python-dotenv
```

### "Database not found" in Compass

**This is normal!** MongoDB creates databases on first write.
The database will appear after:
- Flask app starts (creates collections)
- OR first document is inserted

---

## Success Criteria

✅ **Ready to proceed when:**

1. Test script completes successfully
2. Flask app starts and shows "MongoDB connection is healthy"
3. Health endpoint returns `"connected": true`
4. No authentication or timeout errors

---

## Next Steps After Successful Test

1. ✅ MongoDB Atlas configured and tested
2. ➡️ **Next:** Install remaining Python packages
3. ➡️ **Then:** Start implementing Phase 2 (CRUD operations)

---

## Security Reminder

- ✅ `.env` is in `.gitignore`
- ✅ Never commit credentials to Git
- ✅ Use strong database passwords
- ✅ Limit IP access in production
- ✅ Rotate passwords periodically

---

**Quick Test Command:**
```powershell
cd backend
python test_mongodb_atlas.py
```

**If test passes, you're ready to proceed!**


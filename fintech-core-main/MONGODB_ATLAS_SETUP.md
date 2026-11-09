# MongoDB Atlas Setup Guide - FinCore Analytics

**Last Updated:** October 26, 2026  
**Purpose:** Configure MongoDB Atlas for FinCore Analytics backend

---

## Step-by-Step Atlas Configuration

### 1. Create MongoDB Atlas Account

1. Visit: **https://www.mongodb.com/cloud/atlas/register**
2. Sign up with:
   - Email address
   - OR Google/GitHub account
3. Verify your email if prompted
4. Complete account setup

---

### 2. Create a Free Cluster (M0)

1. **After login, click:** "Create a Deployment" or "Build a Database"

2. **Select Deployment Type:**
   - Choose: **Shared (FREE)**
   - Tier: **M0 Sandbox** (512 MB storage, free forever)

3. **Choose Cloud Provider & Region:**
   - Provider: AWS, Google Cloud, or Azure (any works)
   - Region: **Select closest to your location** for better performance
   - Example: `us-east-1` (N. Virginia) or `eu-west-1` (Ireland)

4. **Cluster Name:**
   - Default: `Cluster0`
   - Or custom: `fincore-analytics-cluster`

5. **Click:** "Create Deployment" (may take 1-3 minutes)

---

### 3. Create Database User

**IMPORTANT:** This is NOT your Atlas account login!

1. **Security Quickstart appears automatically**, or go to:
   - **Database** → **Database Access** → **Add New Database User**

2. **Authentication Method:**
   - Select: **Password**

3. **User Credentials:**
   ```
   Username: fincore_user
   Password: [Generate secure password] ← Click "Autogenerate Secure Password"
   ```
   
   **SAVE THIS PASSWORD IMMEDIATELY!** You cannot view it again.
   
   Example generated password: `xK9mP2nQ7vL4sW8h`

4. **Database User Privileges:**
   - Select: **Read and write to any database**
   - Or custom: `readWrite@finance_advisor`

5. **Click:** "Add User"

---

### 4. Configure Network Access (IP Whitelist)

**CRITICAL:** Atlas blocks all connections by default.

#### Option A: Allow Your Current IP (RECOMMENDED for development)

1. Go to: **Network Access** → **Add IP Address**

2. **Add Your Current IP:**
   - Click: "Add Current IP Address"
   - Description: "My Development Machine"
   - **Note:** This IP may change if you restart your router

3. **Click:** "Confirm"

#### Option B: Allow All IPs (NOT RECOMMENDED for production)

1. Go to: **Network Access** → **Add IP Address**

2. **Allow Access from Anywhere:**
   - Click: "Allow Access from Anywhere"
   - IP Address: `0.0.0.0/0` (automatically filled)
   - Description: "Development - Temporary"
   
   ⚠️ **WARNING:** Only use during development. Remove before production!

3. **Click:** "Confirm"

#### Option C: Specific IP Addresses (BEST for production)

1. **Find Your Public IP:**
   - Visit: https://whatismyipaddress.com/
   - Copy your IPv4 address (e.g., `203.0.113.45`)

2. **Add IP to Whitelist:**
   - Go to: **Network Access** → **Add IP Address**
   - Enter your IP: `203.0.113.45/32`
   - Description: "My Office/Home IP"

3. **Click:** "Confirm"

**Status Check:** IP addresses show "Active" status after ~1 minute.

---

### 5. Get Your Connection String

1. **Go to:** **Database** → **Clusters** → Click **"Connect"** button

2. **Choose Connection Method:**
   - Select: **"Drivers"**

3. **Select Driver:**
   - Driver: **Python**
   - Version: **3.6 or later**

4. **Copy Connection String:**
   
   You'll see something like:
   ```
   mongodb+srv://fincore_user:<password>@cluster0.abc123.mongodb.net/?retryWrites=true&w=majority
   ```

5. **Replace `<password>` placeholder:**
   - Replace `<password>` with your actual database user password
   - **Do NOT use angle brackets `< >`**
   
   Example:
   ```
   # WRONG (has placeholder):
   mongodb+srv://fincore_user:<password>@cluster0.abc123.mongodb.net/?retryWrites=true&w=majority
   
   # CORRECT (password replaced):
   mongodb+srv://fincore_user:xK9mP2nQ7vL4sW8h@cluster0.abc123.mongodb.net/?retryWrites=true&w=majority
   ```

6. **SAVE THIS CONNECTION STRING!** You'll need it for `.env` file.

---

### 6. Optional: Add Database Name to Connection String

Atlas connection string doesn't include the database name. You can either:

**Option A:** Keep database name in separate env variable (CURRENT setup)
```
MONGODB_URI=mongodb+srv://fincore_user:xK9mP2nQ7vL4sW8h@cluster0.abc123.mongodb.net/?retryWrites=true&w=majority
MONGODB_DB_NAME=finance_advisor
```

**Option B:** Add database name to connection string
```
MONGODB_URI=mongodb+srv://fincore_user:xK9mP2nQ7vL4sW8h@cluster0.abc123.mongodb.net/finance_advisor?retryWrites=true&w=majority
```

**RECOMMENDATION:** Use Option A (current setup) for flexibility.

---

## Security Checklist

Before proceeding, verify:

- [ ] Database user created with password saved
- [ ] Network access configured (IP whitelisted)
- [ ] Connection string copied and password replaced
- [ ] `.env` file is listed in `.gitignore`
- [ ] No credentials hardcoded in source files
- [ ] Strong password used (not `password123`)

---

## Common Issues & Solutions

### Issue: "Authentication failed"
**Cause:** Wrong password or username  
**Solution:** 
- Verify username in connection string matches database user
- Recreate database user with new password if lost

### Issue: "Connection timeout"
**Cause:** IP not whitelisted  
**Solution:**
- Add your current IP to Network Access
- Wait 1-2 minutes for changes to propagate
- Check your firewall isn't blocking outbound port 27017

### Issue: "Server selection timeout"
**Cause:** Network connectivity or firewall  
**Solution:**
- Verify internet connection
- Check corporate firewall (may block MongoDB Atlas)
- Try adding `0.0.0.0/0` temporarily to test

### Issue: "Invalid connection string"
**Cause:** Special characters not URL-encoded  
**Solution:**
- If password contains special chars like `@`, `#`, `:`, `/`
- URL-encode them:
  - `@` → `%40`
  - `#` → `%23`
  - `:` → `%3A`
  - `/` → `%2F`
- Example: Password `pass@word` becomes `pass%40word`

---

## Atlas Free Tier Limits

**M0 (Free) Cluster Limits:**
- Storage: 512 MB
- RAM: Shared
- vCPU: Shared
- Connections: 500 concurrent max
- Suitable for: Development, prototyping, small apps

**Sufficient for FinCore Analytics?** ✓ YES
- Estimated data: ~1-10 MB (thousands of transactions)
- Concurrent users: 1 (single-user demo app)
- Free tier is more than adequate

---

## What Gets Created Automatically

When you first connect and run the Flask app:

1. **Database:** `finance_advisor` (created on first write)
2. **Collections:** Created automatically by `db_connection.py`:
   - `income`
   - `expenses`
   - `budgets`
   - `ml_models`
   - `alerts`
   - `settings`
3. **Indexes:** Created for performance optimization

You don't need to create these manually!

---

## Next Steps

After completing Atlas setup:

1. Copy your connection string
2. Update `backend/.env` file (see next section)
3. Run connection test script
4. Verify Flask application starts successfully

---

## Support Resources

- **Atlas Documentation:** https://docs.atlas.mongodb.com/
- **Connection Troubleshooting:** https://docs.atlas.mongodb.com/troubleshoot-connection/
- **Support Forum:** https://www.mongodb.com/community/forums/
- **Connection String Format:** https://docs.mongodb.com/manual/reference/connection-string/

---

**Setup Time:** 10-15 minutes  
**Cost:** $0 (Free M0 tier)  
**Difficulty:** ⭐⭐ (Easy)


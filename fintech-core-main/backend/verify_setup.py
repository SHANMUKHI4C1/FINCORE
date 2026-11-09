"""
Quick verification script to check if Phase 1 setup is correct.
Run this to verify backend installation.
"""

import sys
import os

print("=" * 60)
print("Phase 1 Verification Script")
print("=" * 60)
print()

# Check Python version
print("1. Checking Python version...")
if sys.version_info < (3, 9):
    print("   ❌ Python 3.9+ required. Current:", sys.version)
    sys.exit(1)
else:
    print(f"   ✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

# Check required modules
print("\n2. Checking required Python packages...")
required_packages = [
    'flask',
    'flask_cors',
    'pymongo',
    'dotenv',
    'pandas',
    'numpy',
    'sklearn',
]

missing_packages = []
for package in required_packages:
    try:
        if package == 'flask_cors':
            __import__('flask_cors')
        elif package == 'dotenv':
            __import__('dotenv')
        elif package == 'sklearn':
            __import__('sklearn')
        else:
            __import__(package)
        print(f"   ✅ {package} installed")
    except ImportError:
        print(f"   ❌ {package} NOT installed")
        missing_packages.append(package)

if missing_packages:
    print(f"\n   Missing packages: {', '.join(missing_packages)}")
    print("   Run: pip install -r requirements.txt")
    sys.exit(1)

# Check .env file
print("\n3. Checking .env file...")
if os.path.exists('.env'):
    print("   ✅ .env file exists")
else:
    print("   ❌ .env file not found")
    print("   Copy .env.example to .env and configure it")
    sys.exit(1)

# Check MongoDB connection
print("\n4. Testing MongoDB connection...")
try:
    from pymongo import MongoClient
    from dotenv import load_dotenv
    
    load_dotenv()
    uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
    
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    print(f"   ✅ MongoDB connected at {uri}")
    client.close()
except Exception as e:
    print(f"   ❌ MongoDB connection failed: {str(e)}")
    print("   Make sure MongoDB is running (mongod command)")

# Check directory structure
print("\n5. Checking directory structure...")
required_dirs = [
    'api', 'services', 'models', 'ml', 'ml/saved_models',
    'analytics', 'analytics/data',
    'notifications', 'rag', 'rag/documents', 'rag/embeddings',
    'utils', 'reports', 'reports/output', 'tests'
]

for dir_name in required_dirs:
    if os.path.isdir(dir_name):
        print(f"   ✅ {dir_name}/ exists")
    else:
        print(f"   ❌ {dir_name}/ missing")

# Check config files
print("\n6. Checking configuration files...")
config_files = ['config.py', 'app.py', 'requirements.txt', '.env.example']

for file_name in config_files:
    if os.path.isfile(file_name):
        print(f"   ✅ {file_name} exists")
    else:
        print(f"   ❌ {file_name} missing")

# Try to import main modules
print("\n7. Testing module imports...")
try:
    from config import Config
    print("   ✅ config module imports successfully")
    
    from utils.db_connection import get_db, test_db_connection
    print("   ✅ db_connection module imports successfully")
    
    # Test DB connection function
    success, message = test_db_connection()
    if success:
        print(f"   ✅ Database connection test: {message}")
    else:
        print(f"   ⚠️ Database connection test: {message}")
    
except Exception as e:
    print(f"   ❌ Import error: {str(e)}")

print("\n" + "=" * 60)
print("Verification Complete!")
print("=" * 60)
print("\nIf all checks passed, you can start the Flask server:")
print("  python app.py")
print("\nThen visit: http://localhost:5000/api/health")

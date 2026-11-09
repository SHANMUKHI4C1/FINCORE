"""
MongoDB Atlas Connection Test Script
Tests database connectivity without exposing credentials in logs.
"""

import sys
import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_mongodb_connection():
    """
    Test MongoDB Atlas connection with security in mind.
    Does not print credentials or sensitive information.
    """
    print("=" * 60)
    print("MongoDB Atlas Connection Test")
    print("=" * 60)
    print()
    
    # Get connection details from environment
    mongodb_uri = os.getenv('MONGODB_URI')
    db_name = os.getenv('MONGODB_DB_NAME', 'finance_advisor')
    
    # Validate environment variables
    if not mongodb_uri:
        print("❌ FAIL: MONGODB_URI not set in .env file")
        print()
        print("Action Required:")
        print("1. Ensure .env file exists in backend/ directory")
        print("2. Add MONGODB_URI to .env file")
        print("3. See CONFIGURE_ENV_FILE.md for instructions")
        return False
    
    # Check if it's Atlas or local
    is_atlas = mongodb_uri.startswith('mongodb+srv://')
    is_local = mongodb_uri.startswith('mongodb://localhost')
    
    print(f"Database Name: {db_name}")
    print(f"Connection Type: {'MongoDB Atlas' if is_atlas else 'Local MongoDB' if is_local else 'MongoDB'}")
    
    # Mask URI for display (show only cluster info, hide credentials)
    if is_atlas:
        try:
            # Extract cluster hostname without credentials
            cluster_part = mongodb_uri.split('@')[1].split('/')[0] if '@' in mongodb_uri else 'unknown'
            print(f"Cluster: {cluster_part}")
        except:
            print("Cluster: [parsing error]")
    
    print()
    print("Testing connection...")
    print()
    
    try:
        # Create MongoDB client with timeouts
        client = MongoClient(
            mongodb_uri,
            serverSelectionTimeoutMS=10000,  # 10 second timeout
            connectTimeoutMS=10000,
            socketTimeoutMS=10000
        )
        
        # Test connection with ping
        print("Step 1/4: Attempting connection...")
        client.admin.command('ping')
        print("✓ Connection successful")
        print()
        
        # Get database
        print("Step 2/4: Accessing database...")
        db = client[db_name]
        print(f"✓ Database '{db_name}' accessible")
        print()
        
        # List collections (will be empty initially)
        print("Step 3/4: Checking collections...")
        collections = db.list_collection_names()
        if collections:
            print(f"✓ Found {len(collections)} collections:")
            for col in collections:
                print(f"  - {col}")
        else:
            print("✓ No collections yet (will be created on first write)")
        print()
        
        # Test write permission
        print("Step 4/4: Testing write permission...")
        test_collection = db['_connection_test']
        test_doc = {'test': 'connection', 'timestamp': 'test'}
        result = test_collection.insert_one(test_doc)
        
        if result.inserted_id:
            print("✓ Write permission confirmed")
            # Clean up test document
            test_collection.delete_one({'_id': result.inserted_id})
            print("✓ Test document cleaned up")
        print()
        
        # Close connection
        client.close()
        
        print("=" * 60)
        print("✅ ALL TESTS PASSED")
        print("=" * 60)
        print()
        print("MongoDB Atlas is properly configured!")
        print("You can now start the Flask application.")
        print()
        
        return True
        
    except ServerSelectionTimeoutError as e:
        print("❌ FAIL: Connection timeout")
        print()
        print("Possible causes:")
        print("1. IP address not whitelisted in Atlas Network Access")
        print("2. Firewall blocking outbound connections")
        print("3. Internet connectivity issues")
        print("4. Incorrect cluster hostname")
        print()
        print("Troubleshooting:")
        print("- Check MongoDB Atlas → Network Access")
        print("- Add your current IP or 0.0.0.0/0 for testing")
        print("- Wait 1-2 minutes after adding IP")
        print("- Check your internet connection")
        print()
        print(f"Technical details: {type(e).__name__}")
        return False
        
    except ConnectionFailure as e:
        error_msg = str(e).lower()
        
        if 'authentication failed' in error_msg or 'auth' in error_msg:
            print("❌ FAIL: Authentication error")
            print()
            print("Possible causes:")
            print("1. Incorrect username or password in connection string")
            print("2. Database user not created in Atlas")
            print("3. Special characters not URL-encoded in password")
            print()
            print("Troubleshooting:")
            print("- Verify database username matches Atlas user")
            print("- Check password is correct (case-sensitive)")
            print("- URL-encode special characters (@, #, :, /, etc.)")
            print("- See CONFIGURE_ENV_FILE.md for encoding guide")
        else:
            print("❌ FAIL: Connection error")
            print()
            print(f"Error: {str(e)}")
            print()
            print("Check your MONGODB_URI in .env file")
        
        print()
        return False
        
    except Exception as e:
        print(f"❌ FAIL: Unexpected error")
        print()
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print()
        print("If issue persists, check:")
        print("- .env file syntax (no extra spaces)")
        print("- Connection string format")
        print("- MongoDB Atlas status page")
        print()
        return False


if __name__ == '__main__':
    success = test_mongodb_connection()
    sys.exit(0 if success else 1)

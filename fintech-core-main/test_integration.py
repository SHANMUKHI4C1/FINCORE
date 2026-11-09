"""
Integration Test Script for React-to-Flask Communication
Tests the health endpoint and MongoDB connectivity reporting.
"""

import requests
import json
from datetime import datetime

def test_flask_health_endpoint():
    """Test Flask health endpoint directly."""
    print("=" * 60)
    print("INTEGRATION TEST: React-to-Flask Communication")
    print("=" * 60)
    print(f"\nTest Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    results = {
        'flask_startup': 'NOT TESTED',
        'react_startup': 'NOT TESTED',
        'api_proxy': 'NOT TESTED',
        'react_to_flask': 'NOT TESTED',
        'mongodb_connectivity': 'NOT TESTED'
    }
    
    # Test 1: Flask Health Endpoint (Direct)
    print("Test 1: Flask Backend Health Endpoint")
    print("-" * 60)
    try:
        response = requests.get('http://127.0.0.1:5000/api/health', timeout=10)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
            results['flask_startup'] = 'PASS'
            
            # Check MongoDB connectivity in response
            if 'database' in data:
                db_connected = data['database'].get('connected', False)
                if db_connected:
                    results['mongodb_connectivity'] = 'PASS'
                    print(f"\n✓ MongoDB Connected: {db_connected}")
                    print(f"  Database Name: {data['database'].get('database_name', 'N/A')}")
                else:
                    results['mongodb_connectivity'] = 'FAIL'
                    print(f"\n✗ MongoDB Not Connected")
            
            # Check features
            if 'features' in data:
                print(f"\nFeature Flags:")
                for key, value in data['features'].items():
                    print(f"  {key}: {value}")
        else:
            results['flask_startup'] = 'FAIL'
            print(f"✗ Health endpoint returned status {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        results['flask_startup'] = 'FAIL'
        print("✗ Could not connect to Flask backend at http://127.0.0.1:5000")
        print("  Make sure Flask is running: python backend/app.py")
    except Exception as e:
        results['flask_startup'] = 'FAIL'
        print(f"✗ Error testing Flask endpoint: {str(e)}")
    
    print("\n")
    
    # Test 2: Check if React dev server is running
    print("Test 2: React Development Server")
    print("-" * 60)
    try:
        response = requests.get('http://localhost:5173', timeout=5)
        if response.status_code == 200:
            results['react_startup'] = 'PASS'
            print("✓ React dev server is running at http://localhost:5173")
        else:
            results['react_startup'] = 'FAIL'
            print(f"✗ React dev server returned status {response.status_code}")
    except requests.exceptions.ConnectionError:
        results['react_startup'] = 'FAIL'
        print("✗ React dev server is not running at http://localhost:5173")
        print("  Start it with: cd frontend && npm run dev")
    except Exception as e:
        results['react_startup'] = 'FAIL'
        print(f"✗ Error checking React server: {str(e)}")
    
    print("\n")
    
    # Test 3: Test Vite Proxy (simulating frontend request)
    print("Test 3: Vite Proxy Configuration")
    print("-" * 60)
    print("Testing if /api requests are proxied from React to Flask...")
    
    try:
        # Try to access through Vite proxy
        response = requests.get('http://localhost:5173/api/health', timeout=10)
        if response.status_code == 200:
            data = response.json()
            results['api_proxy'] = 'PASS'
            results['react_to_flask'] = 'PASS'
            print("✓ Vite proxy successfully forwarded request to Flask")
            print(f"  Response from Flask through proxy: {json.dumps(data, indent=2)}")
        else:
            results['api_proxy'] = 'FAIL'
            results['react_to_flask'] = 'FAIL'
            print(f"✗ Proxy request returned status {response.status_code}")
    except requests.exceptions.ConnectionError:
        results['api_proxy'] = 'FAIL'
        results['react_to_flask'] = 'FAIL'
        print("✗ Could not connect through Vite proxy")
        print("  This could mean:")
        print("  1. React dev server is not running")
        print("  2. Vite proxy is not configured correctly")
        print("  3. Flask backend is not accessible")
    except Exception as e:
        results['api_proxy'] = 'FAIL'
        results['react_to_flask'] = 'FAIL'
        print(f"✗ Error testing proxy: {str(e)}")
    
    # Summary
    print("\n")
    print("=" * 60)
    print("INTEGRATION TEST SUMMARY")
    print("=" * 60)
    print(f"React Startup:            {results['react_startup']}")
    print(f"Flask Startup:            {results['flask_startup']}")
    print(f"API Proxy:                {results['api_proxy']}")
    print(f"React-to-Flask Comm:      {results['react_to_flask']}")
    print(f"MongoDB Connectivity:     {results['mongodb_connectivity']}")
    print("=" * 60)
    
    # Check overall status
    all_pass = all(status == 'PASS' for status in results.values())
    if all_pass:
        print("\n✓ ALL TESTS PASSED - Integration is working correctly!")
    else:
        failed = [k for k, v in results.items() if v == 'FAIL']
        not_tested = [k for k, v in results.items() if v == 'NOT TESTED']
        print(f"\n✗ INTEGRATION ISSUES DETECTED")
        if failed:
            print(f"  Failed: {', '.join(failed)}")
        if not_tested:
            print(f"  Not Tested: {', '.join(not_tested)}")
    
    print("\n")
    return results

if __name__ == '__main__':
    test_flask_health_endpoint()

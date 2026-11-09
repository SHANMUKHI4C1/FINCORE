"""
Verify installed packages against requirements.
"""
import sys
import importlib.util

# Required packages from requirements.txt
required_packages = {
    'flask': ('Flask', '3.0.0'),
    'flask_cors': ('Flask-CORS', '4.0.0'),
    'werkzeug': ('Werkzeug', '3.0.1'),
    'pymongo': ('PyMongo', '4.6.1'),
    'dotenv': ('python-dotenv', '1.0.0'),
    'pandas': ('pandas', '2.2.0'),
    'numpy': ('NumPy', '1.26.0'),
    'sklearn': ('scikit-learn', '1.4.0'),
    'joblib': ('joblib', '1.3.0'),
    'matplotlib': ('matplotlib', '3.8.0'),
    'reportlab': ('ReportLab', '4.0.7'),
    'twilio': ('Twilio', '8.11.0'),
    'pytest': ('pytest', '7.4.3'),
    'dateutil': ('python-dateutil', '2.8.2'),
}

print("=" * 70)
print("BACKEND PACKAGE VERIFICATION")
print("=" * 70)
print()

installed = []
missing = []
version_mismatch = []

for module_name, (display_name, min_version) in required_packages.items():
    try:
        spec = importlib.util.find_spec(module_name)
        if spec:
            mod = importlib.import_module(module_name)
            version = getattr(mod, '__version__', 'unknown')
            status = "✓ INSTALLED"
            installed.append((display_name, version))
            print(f"{status:15} {display_name:25} {version}")
        else:
            missing.append((display_name, min_version))
            print(f"✗ MISSING:    {display_name:25} (required: {min_version})")
    except Exception as e:
        missing.append((display_name, min_version))
        print(f"✗ MISSING:    {display_name:25} (required: {min_version})")

print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"Installed: {len(installed)}")
print(f"Missing:   {len(missing)}")
print()

if missing:
    print("MISSING PACKAGES:")
    for pkg, version in missing:
        print(f"  - {pkg} (>={version})")
    print()
    sys.exit(1)
else:
    print("✅ ALL REQUIRED PACKAGES INSTALLED")
    sys.exit(0)

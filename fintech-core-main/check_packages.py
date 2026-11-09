import importlib.util
packages = {
    'numpy': 'NumPy',
    'pandas': 'Pandas', 
    'sklearn': 'scikit-learn',
    'flask': 'Flask',
    'pymongo': 'PyMongo',
    'flask_cors': 'Flask-CORS',
    'dotenv': 'python-dotenv',
    'reportlab': 'ReportLab',
    'twilio': 'Twilio',
    'joblib': 'joblib'
}

for pkg, name in packages.items():
    try:
        spec = importlib.util.find_spec(pkg)
        if spec:
            mod = importlib.import_module(pkg)
            version = getattr(mod, '__version__', 'unknown')
            print(f'✓ {name}: {version}')
        else:
            print(f'✗ {name}: NOT INSTALLED')
    except Exception as e:
        print(f'✗ {name}: NOT INSTALLED')

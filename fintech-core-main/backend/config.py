"""
Configuration module for Flask application.
Loads environment variables and provides configuration classes.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration class."""
    
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = os.getenv('FLASK_DEBUG', '1') == '1'
    PORT = int(os.getenv('FLASK_PORT', 5000))
    
    # MongoDB Configuration
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
    MONGODB_DB_NAME = os.getenv('MONGODB_DB_NAME', 'finance_advisor')
    
    # Analytics Configuration
    ANALYTICS_ENABLED = os.getenv('ANALYTICS_ENABLED', 'true').lower() == 'true'
    
    # Twilio SMS Configuration
    SMS_ENABLED = os.getenv('SMS_ENABLED', 'false').lower() == 'true'
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', '')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', '')
    TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER', '')
    USER_PHONE_NUMBER = os.getenv('USER_PHONE_NUMBER', '')
    
    # ML Configuration
    ML_TRAINING_MIN_SAMPLES = int(os.getenv('ML_TRAINING_MIN_SAMPLES', 50))
    ML_MODEL_DIR = os.getenv('ML_MODEL_DIR', './ml/saved_models/')
    
    # Reports Configuration
    REPORTS_OUTPUT_DIR = os.getenv('REPORTS_OUTPUT_DIR', './reports/output/')
    
    # RAG Configuration (Optional)
    RAG_ENABLED = os.getenv('RAG_ENABLED', 'false').lower() == 'true'
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    RAG_MODEL = os.getenv('RAG_MODEL', 'gpt-3.5-turbo')
    RAG_TEMPERATURE = float(os.getenv('RAG_TEMPERATURE', 0.7))
    RAG_MAX_TOKENS = int(os.getenv('RAG_MAX_TOKENS', 500))
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    @staticmethod
    def validate_config():
        """
        Validate configuration and warn about missing optional components.
        Returns tuple: (is_valid, warnings_list)
        """
        warnings = []
        
        # Check MongoDB connection string
        if not Config.MONGODB_URI:
            return False, ["MongoDB URI is required"]
        
        # Warn about optional features
        if not Config.ANALYTICS_ENABLED:
            warnings.append("Analytics module is disabled")
        
        if not Config.SMS_ENABLED:
            warnings.append("SMS alerts are disabled - configure Twilio to enable")
        elif not Config.TWILIO_ACCOUNT_SID or not Config.TWILIO_AUTH_TOKEN:
            warnings.append("SMS enabled but Twilio credentials missing - alerts will fail")
        
        if not Config.RAG_ENABLED:
            warnings.append("RAG assistant is disabled - enable in .env to use this feature")
        
        return True, warnings


class DevelopmentConfig(Config):
    """Development environment configuration."""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production environment configuration."""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing environment configuration."""
    DEBUG = True
    TESTING = True
    MONGODB_DB_NAME = 'finance_advisor_test'


# Configuration dictionary
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config(env_name=None):
    """
    Get configuration object based on environment name.
    
    Args:
        env_name (str): Environment name ('development', 'production', 'testing')
        
    Returns:
        Config: Configuration object
    """
    if env_name is None:
        env_name = os.getenv('FLASK_ENV', 'development')
    
    return config_by_name.get(env_name, DevelopmentConfig)

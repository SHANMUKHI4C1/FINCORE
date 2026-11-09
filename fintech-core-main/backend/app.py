"""
Main Flask application for AI-Based Personal Finance Advisor.
Entry point for the backend API server.
"""

import os
import logging
from flask import Flask, jsonify
from flask_cors import CORS
from config import get_config, Config
from utils.db_connection import get_db, test_db_connection, close_db_connection

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def create_app(config_name=None):
    """
    Application factory pattern.
    
    Args:
        config_name (str): Configuration name ('development', 'production', 'testing')
        
    Returns:
        Flask: Configured Flask application
    """
    app = Flask(__name__)
    
    # Load configuration
    config = get_config(config_name)
    app.config.from_object(config)
    
    # Enable CORS for frontend
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:5173", "http://localhost:3000"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Validate configuration
    is_valid, warnings = Config.validate_config()
    if not is_valid:
        logger.error("Invalid configuration")
        for warning in warnings:
            logger.error(f"  - {warning}")
        raise ValueError("Invalid configuration")
    
    # Log warnings
    if warnings:
        logger.warning("Configuration warnings:")
        for warning in warnings:
            logger.warning(f"  - {warning}")
    
    # Test database connection
    try:
        db = get_db()
        success, message = test_db_connection()
        if success:
            logger.info(message)
        else:
            logger.error(message)
            raise ConnectionError(message)
    except Exception as e:
        logger.error(f"Failed to connect to database: {str(e)}")
        raise
    
    # Register blueprints (API routes)
    # Note: These will be uncommented as we implement each phase
    # from api.income_routes import income_bp
    # from api.expense_routes import expense_bp
    # from api.ml_routes import ml_bp
    # from api.analytics_routes import analytics_bp
    # from api.report_routes import report_bp
    # from api.alert_routes import alert_bp
    # from api.rag_routes import rag_bp
    
    # app.register_blueprint(income_bp, url_prefix='/api/income')
    # app.register_blueprint(expense_bp, url_prefix='/api/expenses')
    # app.register_blueprint(ml_bp, url_prefix='/api/ml')
    # app.register_blueprint(analytics_bp, url_prefix='/api/analytics')
    # app.register_blueprint(report_bp, url_prefix='/api/reports')
    # app.register_blueprint(alert_bp, url_prefix='/api/alerts')
    # app.register_blueprint(rag_bp, url_prefix='/api/rag')
    
    # Health check endpoint
    @app.route('/api/health', methods=['GET'])
    def health_check():
        """Health check endpoint to verify server is running."""
        db_success, db_message = test_db_connection()
        
        return jsonify({
            'status': 'healthy',
            'message': 'AI-Based Personal Finance Advisor API is running',
            'database': {
                'connected': db_success,
                'message': db_message
            },
            'features': {
                'analytics_enabled': Config.ANALYTICS_ENABLED,
                'sms_enabled': Config.SMS_ENABLED,
                'rag_enabled': Config.RAG_ENABLED
            }
        }), 200
    
    # Root endpoint
    @app.route('/', methods=['GET'])
    def root():
        """Root endpoint with API information."""
        return jsonify({
            'name': 'AI-Based Personal Finance Advisor API',
            'version': '1.0.0',
            'description': 'Backend API for personal finance management with ML and Python analytics',
            'endpoints': {
                'health': '/api/health',
                'income': '/api/income (coming in Phase 2)',
                'expenses': '/api/expenses (coming in Phase 2)',
                'ml': '/api/ml (coming in Phase 3)',
                'analytics': '/api/analytics (coming in Phase 4)',
                'reports': '/api/reports (coming in Phase 6)',
                'alerts': '/api/alerts (coming in Phase 6)',
                'rag': '/api/rag (optional, Phase 9)'
            }
        }), 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors."""
        return jsonify({
            'error': 'Not Found',
            'message': 'The requested resource was not found',
            'code': 404
        }), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors."""
        logger.error(f"Internal server error: {str(error)}")
        return jsonify({
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred',
            'code': 500
        }), 500
    
    @app.errorhandler(Exception)
    def handle_exception(error):
        """Handle all unhandled exceptions."""
        logger.error(f"Unhandled exception: {str(error)}", exc_info=True)
        return jsonify({
            'error': 'Internal Server Error',
            'message': str(error),
            'code': 500
        }), 500
    
    # Cleanup on shutdown
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        """Close database connection on shutdown."""
        close_db_connection()
    
    return app


# Create application instance
app = create_app()


if __name__ == '__main__':
    """Run the Flask application."""
    port = Config.PORT
    debug = Config.DEBUG
    
    logger.info(f"Starting Flask application on port {port}")
    logger.info(f"Environment: {Config.FLASK_ENV}")
    logger.info(f"Debug mode: {debug}")
    logger.info(f"Database: {Config.MONGODB_DB_NAME}")
    
    # Run the application
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )

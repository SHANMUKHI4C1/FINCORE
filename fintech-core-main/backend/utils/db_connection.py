"""
MongoDB database connection utility.
Provides singleton database connection and collection access.
"""

from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
import logging
from config import Config

logger = logging.getLogger(__name__)


class DatabaseConnection:
    """Singleton class for MongoDB connection management."""
    
    _instance = None
    _client = None
    _db = None
    
    def __new__(cls):
        """Ensure only one instance of DatabaseConnection exists."""
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialize database connection if not already connected."""
        if self._client is None:
            self.connect()
    
    def connect(self):
        """
        Establish connection to MongoDB.
        
        Raises:
            ConnectionFailure: If unable to connect to MongoDB
        """
        try:
            logger.info(f"Connecting to MongoDB at {Config.MONGODB_URI}")
            
            # Create MongoDB client with timeout
            self._client = MongoClient(
                Config.MONGODB_URI,
                serverSelectionTimeoutMS=5000,  # 5 second timeout
                connectTimeoutMS=5000
            )
            
            # Test connection
            self._client.admin.command('ping')
            
            # Get database
            self._db = self._client[Config.MONGODB_DB_NAME]
            
            logger.info(f"Successfully connected to MongoDB database: {Config.MONGODB_DB_NAME}")
            
            # Create indexes and validation rules
            self._setup_database()
            
        except (ConnectionFailure, ServerSelectionTimeoutError) as e:
            logger.error(f"Failed to connect to MongoDB: {str(e)}")
            raise ConnectionFailure(f"Could not connect to MongoDB at {Config.MONGODB_URI}. "
                                   f"Please ensure MongoDB is running. Error: {str(e)}")
    
    def _setup_database(self):
        """
        Set up database collections with indexes and validation rules.
        This runs only once when connection is first established.
        """
        try:
            # Income collection indexes
            income_collection = self._db['income']
            income_collection.create_index([('date', DESCENDING)])
            income_collection.create_index([('source', ASCENDING), ('date', DESCENDING)])
            logger.info("Created indexes for 'income' collection")
            
            # Expenses collection indexes
            expenses_collection = self._db['expenses']
            expenses_collection.create_index([('date', DESCENDING)])
            expenses_collection.create_index([('category', ASCENDING), ('date', DESCENDING)])
            expenses_collection.create_index([('is_anomaly', ASCENDING)])
            logger.info("Created indexes for 'expenses' collection")
            
            # Budgets collection indexes
            budgets_collection = self._db['budgets']
            budgets_collection.create_index([('month', DESCENDING), ('category', ASCENDING)], unique=True)
            logger.info("Created indexes for 'budgets' collection")
            
            # ML models collection
            ml_models_collection = self._db['ml_models']
            ml_models_collection.create_index([('model_name', ASCENDING)], unique=True)
            logger.info("Created indexes for 'ml_models' collection")
            
            # Alerts collection indexes
            alerts_collection = self._db['alerts']
            alerts_collection.create_index([('triggered_at', DESCENDING)])
            alerts_collection.create_index([('alert_type', ASCENDING)])
            logger.info("Created indexes for 'alerts' collection")
            
            # Settings collection (for user preferences)
            settings_collection = self._db['settings']
            logger.info("Initialized 'settings' collection")
            
            logger.info("Database setup completed successfully")
            
        except Exception as e:
            logger.warning(f"Error during database setup: {str(e)}")
            # Don't raise - indexes might already exist
    
    @property
    def db(self):
        """
        Get database instance.
        
        Returns:
            Database: MongoDB database instance
        """
        if self._db is None:
            self.connect()
        return self._db
    
    @property
    def client(self):
        """
        Get MongoDB client instance.
        
        Returns:
            MongoClient: MongoDB client instance
        """
        if self._client is None:
            self.connect()
        return self._client
    
    def get_collection(self, collection_name):
        """
        Get a specific collection.
        
        Args:
            collection_name (str): Name of the collection
            
        Returns:
            Collection: MongoDB collection instance
        """
        return self.db[collection_name]
    
    def close(self):
        """Close MongoDB connection."""
        if self._client:
            self._client.close()
            self._client = None
            self._db = None
            logger.info("MongoDB connection closed")
    
    def test_connection(self):
        """
        Test if database connection is working.
        
        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            self.client.admin.command('ping')
            return True, "MongoDB connection is healthy"
        except Exception as e:
            return False, f"MongoDB connection failed: {str(e)}"


# Singleton instance
_db_connection = None


def get_db():
    """
    Get database instance (singleton pattern).
    
    Returns:
        Database: MongoDB database instance
    """
    global _db_connection
    if _db_connection is None:
        _db_connection = DatabaseConnection()
    return _db_connection.db


def get_collection(collection_name):
    """
    Get a specific collection.
    
    Args:
        collection_name (str): Name of the collection
        
    Returns:
        Collection: MongoDB collection instance
    """
    global _db_connection
    if _db_connection is None:
        _db_connection = DatabaseConnection()
    return _db_connection.get_collection(collection_name)


def close_db_connection():
    """Close database connection."""
    global _db_connection
    if _db_connection:
        _db_connection.close()
        _db_connection = None


def test_db_connection():
    """
    Test database connection.
    
    Returns:
        tuple: (success: bool, message: str)
    """
    global _db_connection
    if _db_connection is None:
        _db_connection = DatabaseConnection()
    return _db_connection.test_connection()

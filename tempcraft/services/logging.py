"""Logging service configuration."""
import logging
from tempcraft.config.settings import LOG_FILE

def setup_logging():
    """Configure the application-wide logging."""
    logger = logging.getLogger("tempcraft")
    logger.setLevel(logging.DEBUG)
    
    # Avoid duplicate logs if setup is called multiple times
    if not logger.handlers:
        # File handler
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger

logger = setup_logging()

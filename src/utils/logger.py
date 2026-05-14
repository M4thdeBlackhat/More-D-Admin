"""Logging system for More-D-Admin"""

import logging
import os
from datetime import datetime
import config

class Logger:
    """
    Custom logger class for application-wide logging.
    """
    
    _loggers = {}
    
    def __init__(self, name):
        """
        Initialize logger with name.
        
        Args:
            name (str): Logger name
        """
        self.name = name
        self.logger = self._get_or_create_logger(name)
    
    @staticmethod
    def _get_or_create_logger(name):
        """
        Get or create a logger instance.
        
        Args:
            name (str): Logger name
            
        Returns:
            logging.Logger: Logger instance
        """
        if name in Logger._loggers:
            return Logger._loggers[name]
        
        # Create logs directory if it doesn't exist
        if not os.path.exists(config.LOGS_DIR):
            os.makedirs(config.LOGS_DIR)
        
        # Create logger
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, config.LOG_LEVEL))
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # File handler
        log_file = os.path.join(config.LOGS_DIR, config.LOG_FILE)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(getattr(logging, config.LOG_LEVEL))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        Logger._loggers[name] = logger
        return logger
    
    def info(self, message):
        """Log info message"""
        self.logger.info(message)
    
    def warning(self, message):
        """Log warning message"""
        self.logger.warning(message)
    
    def error(self, message):
        """Log error message"""
        self.logger.error(message)
    
    def debug(self, message):
        """Log debug message"""
        self.logger.debug(message)
    
    def critical(self, message):
        """Log critical message"""
        self.logger.critical(message)

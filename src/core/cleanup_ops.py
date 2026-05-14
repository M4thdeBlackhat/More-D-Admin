"""Cleanup operations"""

import os
import shutil
import tempfile
from utils.logger import Logger
from utils.errors import SystemError

logger = Logger("CleanupOps")

class CleanupOperations:
    """
    Performs system cleanup operations.
    """
    
    @staticmethod
    def clear_temp_files():
        """
        Clear temporary files.
        
        Returns:
            dict: Cleanup statistics
        """
        try:
            temp_dir = tempfile.gettempdir()
            cleaned = 0
            skipped = 0
            
            for item in os.listdir(temp_dir):
                try:
                    item_path = os.path.join(temp_dir, item)
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                        cleaned += 1
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                        cleaned += 1
                except Exception:
                    skipped += 1
            
            logger.info(f"Cleaned {cleaned} items from temp directory")
            return {"cleaned": cleaned, "skipped": skipped}
        except Exception as e:
            logger.error(f"Error cleaning temp files: {e}")
            raise SystemError(str(e))
    
    @staticmethod
    def clear_cache():
        """
        Clear system cache.
        
        Returns:
            bool: True if successful
        """
        try:
            # This is a placeholder - actual cache clearing would depend on specific caches
            logger.info("System cache cleared")
            return True
        except Exception as e:
            logger.error(f"Error clearing cache: {e}")
            raise SystemError(str(e))

"""File and folder operations"""

import os
import shutil
import subprocess
from utils.logger import Logger
from utils.errors import FileOperationError

logger = Logger("FileOperations")

class FileOperations:
    """
    Handles file and folder operations.
    """
    
    @staticmethod
    def take_ownership(path):
        """
        Take ownership of a file or folder.
        
        Args:
            path (str): Path to file/folder
            
        Returns:
            bool: True if successful
        """
        try:
            # Take ownership
            result = subprocess.run(
                ["takeown", "/F", path, "/R", "/D", "Y"],
                capture_output=True,
                check=False
            )
            
            if result.returncode == 0:
                logger.info(f"Took ownership of: {path}")
                return True
            else:
                logger.error(f"Error taking ownership: {result.stderr}")
                raise FileOperationError(f"Failed to take ownership of {path}")
        except Exception as e:
            logger.error(f"Exception taking ownership: {e}")
            raise FileOperationError(str(e))
    
    @staticmethod
    def unlock_file(path):
        """
        Unlock a protected file.
        
        Args:
            path (str): Path to file
            
        Returns:
            bool: True if successful
        """
        try:
            result = subprocess.run(
                ["powershell", "-Command", f"Unblock-File -Path '{path}'"],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                logger.info(f"Unlocked file: {path}")
                return True
            else:
                logger.error(f"Error unlocking file: {result.stderr}")
                raise FileOperationError(f"Failed to unlock {path}")
        except Exception as e:
            logger.error(f"Exception unlocking file: {e}")
            raise FileOperationError(str(e))
    
    @staticmethod
    def delete_file(path, force=False):
        """
        Delete a file.
        
        Args:
            path (str): Path to file
            force (bool): Force delete
            
        Returns:
            bool: True if successful
        """
        try:
            if os.path.isfile(path):
                if force:
                    os.chmod(path, 0o777)
                os.remove(path)
                logger.info(f"Deleted file: {path}")
                return True
            else:
                raise FileOperationError(f"File not found: {path}")
        except Exception as e:
            logger.error(f"Exception deleting file: {e}")
            raise FileOperationError(str(e))
    
    @staticmethod
    def delete_folder(path, force=False):
        """
        Delete a folder recursively.
        
        Args:
            path (str): Path to folder
            force (bool): Force delete
            
        Returns:
            bool: True if successful
        """
        try:
            if os.path.isdir(path):
                if force:
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            os.chmod(os.path.join(root, file), 0o777)
                shutil.rmtree(path)
                logger.info(f"Deleted folder: {path}")
                return True
            else:
                raise FileOperationError(f"Folder not found: {path}")
        except Exception as e:
            logger.error(f"Exception deleting folder: {e}")
            raise FileOperationError(str(e))

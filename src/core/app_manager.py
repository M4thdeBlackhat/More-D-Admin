"""Application management operations"""

import subprocess
from utils.logger import Logger
from utils.errors import ApplicationError

logger = Logger("AppManager")

class ApplicationManager:
    """
    Manages installed applications.
    """
    
    @staticmethod
    def get_installed_apps():
        """
        Get list of installed applications.
        
        Returns:
            list: List of application dictionaries
        """
        try:
            result = subprocess.run(
                ["powershell", "-Command",
                 "Get-WmiObject -Query 'select * from Win32_Product' | ConvertTo-Json"],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                logger.info("Retrieved installed applications")
                return result.stdout
            else:
                logger.error(f"Error getting apps: {result.stderr}")
                raise ApplicationError(result.stderr)
        except Exception as e:
            logger.error(f"Exception getting applications: {e}")
            raise ApplicationError(str(e))
    
    @staticmethod
    def uninstall_app(app_name):
        """
        Uninstall an application.
        
        Args:
            app_name (str): Application name
            
        Returns:
            bool: True if successful
        """
        try:
            result = subprocess.run(
                ["powershell", "-Command",
                 f"Get-WmiObject -Query \"select * from Win32_Product where Name='{app_name}'\" | Invoke-WmiMethod -Name Uninstall"],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                logger.info(f"Uninstalled application: {app_name}")
                return True
            else:
                logger.error(f"Error uninstalling app: {result.stderr}")
                raise ApplicationError(f"Failed to uninstall {app_name}")
        except Exception as e:
            logger.error(f"Exception uninstalling application: {e}")
            raise ApplicationError(str(e))

"""System restore point management"""

import subprocess
import datetime
from utils.logger import Logger
from utils.errors import SystemError

logger = Logger("RestorePoint")

def create_restore_point(description=None):
    """
    Create a system restore point before major operations.
    
    Args:
        description (str): Description for the restore point
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        if description is None:
            description = f"More-D-Admin Restore Point {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        # PowerShell command to create restore point
        ps_command = (
            f'Checkpoint-Computer -Description "{description}" -RestorePointType "MODIFY_SETTINGS"'
        )
        
        result = subprocess.run(
            ["powershell", "-Command", ps_command],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            logger.info(f"Restore point created: {description}")
            return True
        else:
            logger.error(f"Failed to create restore point: {result.stderr}")
            return False
            
    except Exception as e:
        logger.error(f"Error creating restore point: {e}")
        return False

def list_restore_points():
    """
    List available restore points.
    
    Returns:
        list: List of restore point dictionaries
    """
    try:
        ps_command = 'Get-ComputerRestorePoint | Select-Object -Property Description, CreationTime | ConvertTo-Json'
        
        result = subprocess.run(
            ["powershell", "-Command", ps_command],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            logger.info("Retrieved restore points")
            return result.stdout
        else:
            logger.error(f"Failed to list restore points: {result.stderr}")
            return []
            
    except Exception as e:
        logger.error(f"Error listing restore points: {e}")
        return []

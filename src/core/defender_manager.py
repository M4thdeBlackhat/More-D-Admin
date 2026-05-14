"""Defender management operations"""

import subprocess
from utils.logger import Logger
from utils.errors import SystemError

logger = Logger("DefenderManager")

class DefenderManager:
    """
    Manages Windows Defender.
    """
    
    @staticmethod
    def get_defender_status():
        """
        Get Windows Defender status.
        
        Returns:
            dict: Defender status information
        """
        try:
            result = subprocess.run(
                ["powershell", "-Command",
                 "Get-MpComputerStatus | ConvertTo-Json"],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                logger.info("Retrieved Defender status")
                return result.stdout
            else:
                logger.error(f"Error getting Defender status: {result.stderr}")
                raise SystemError(result.stderr)
        except Exception as e:
            logger.error(f"Exception getting Defender status: {e}")
            raise SystemError(str(e))
    
    @staticmethod
    def toggle_realtime_protection(enable):
        """
        Toggle real-time protection.
        
        Args:
            enable (bool): True to enable, False to disable
            
        Returns:
            bool: True if successful
        """
        try:
            state = "$true" if enable else "$false"
            result = subprocess.run(
                ["powershell", "-Command",
                 f"Set-MpPreference -DisableRealtimeMonitoring ${state}"],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                status = "enabled" if enable else "disabled"
                logger.info(f"Real-time protection {status}")
                return True
            else:
                raise SystemError(result.stderr)
        except Exception as e:
            logger.error(f"Error toggling real-time protection: {e}")
            raise SystemError(str(e))

"""Windows service management operations"""

import subprocess
from utils.logger import Logger
from utils.errors import ServiceError

logger = Logger("ServiceManager")

class ServiceManager:
    """
    Manages Windows services.
    """
    
    @staticmethod
    def get_all_services():
        """
        Get all Windows services.
        
        Returns:
            list: List of service dictionaries
        """
        try:
            result = subprocess.run(
                ["powershell", "-Command", "Get-Service | ConvertTo-Json"],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                logger.info("Retrieved all services")
                return result.stdout
            else:
                logger.error(f"Error getting services: {result.stderr}")
                raise ServiceError(result.stderr)
        except Exception as e:
            logger.error(f"Exception getting services: {e}")
            raise ServiceError(str(e))
    
    @staticmethod
    def start_service(service_name):
        """
        Start a Windows service.
        
        Args:
            service_name (str): Name of the service
            
        Returns:
            bool: True if successful
        """
        try:
            result = subprocess.run(
                ["powershell", "-Command", f"Start-Service -Name {service_name}"],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                logger.info(f"Started service: {service_name}")
                return True
            else:
                logger.error(f"Error starting service {service_name}: {result.stderr}")
                raise ServiceError(result.stderr)
        except Exception as e:
            logger.error(f"Exception starting service {service_name}: {e}")
            raise ServiceError(str(e))
    
    @staticmethod
    def stop_service(service_name):
        """
        Stop a Windows service.
        
        Args:
            service_name (str): Name of the service
            
        Returns:
            bool: True if successful
        """
        try:
            result = subprocess.run(
                ["powershell", "-Command", f"Stop-Service -Name {service_name} -Force"],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                logger.info(f"Stopped service: {service_name}")
                return True
            else:
                logger.error(f"Error stopping service {service_name}: {result.stderr}")
                raise ServiceError(result.stderr)
        except Exception as e:
            logger.error(f"Exception stopping service {service_name}: {e}")
            raise ServiceError(str(e))
    
    @staticmethod
    def set_service_startup(service_name, startup_type):
        """
        Set service startup type.
        
        Args:
            service_name (str): Name of the service
            startup_type (str): Startup type (Automatic, Manual, Disabled)
            
        Returns:
            bool: True if successful
        """
        try:
            result = subprocess.run(
                ["powershell", "-Command", 
                 f"Set-Service -Name {service_name} -StartupType {startup_type}"],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                logger.info(f"Set {service_name} startup to {startup_type}")
                return True
            else:
                logger.error(f"Error setting startup for {service_name}: {result.stderr}")
                raise ServiceError(result.stderr)
        except Exception as e:
            logger.error(f"Exception setting service startup: {e}")
            raise ServiceError(str(e))

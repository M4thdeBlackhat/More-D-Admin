"""Registry operations"""

import subprocess
from utils.logger import Logger
from utils.errors import RegistryError

logger = Logger("RegistryOps")

class RegistryOperations:
    """
    Manages Windows Registry operations.
    """
    
    @staticmethod
    def read_registry_key(hive, path, name):
        """
        Read a registry key value.
        
        Args:
            hive (str): Registry hive (HKLM, HKCU, etc.)
            path (str): Registry path
            name (str): Value name
            
        Returns:
            str: Registry value
        """
        try:
            result = subprocess.run(
                ["powershell", "-Command",
                 f"Get-ItemProperty -Path '{hive}:\\{path}' -Name {name}"],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                logger.info(f"Read registry value: {hive}\\{path}\\{name}")
                return result.stdout
            else:
                raise RegistryError(result.stderr)
        except Exception as e:
            logger.error(f"Error reading registry: {e}")
            raise RegistryError(str(e))
    
    @staticmethod
    def write_registry_key(hive, path, name, value):
        """
        Write a registry key value.
        
        Args:
            hive (str): Registry hive
            path (str): Registry path
            name (str): Value name
            value: Value to write
            
        Returns:
            bool: True if successful
        """
        try:
            result = subprocess.run(
                ["powershell", "-Command",
                 f"New-ItemProperty -Path '{hive}:\\{path}' -Name {name} -Value {value} -Force"],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                logger.info(f"Wrote registry value: {hive}\\{path}\\{name}")
                return True
            else:
                raise RegistryError(result.stderr)
        except Exception as e:
            logger.error(f"Error writing registry: {e}")
            raise RegistryError(str(e))

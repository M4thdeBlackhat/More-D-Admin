"""Process management operations"""

import psutil
import subprocess
from utils.logger import Logger
from utils.errors import ProcessError

logger = Logger("ProcessOps")

class ProcessOperations:
    """
    Manages system processes.
    """
    
    @staticmethod
    def get_all_processes():
        """
        Get all running processes.
        
        Returns:
            list: List of process dictionaries
        """
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'status', 'memory_percent']):
                try:
                    processes.append(proc.as_dict())
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            logger.info(f"Retrieved {len(processes)} processes")
            return processes
        except Exception as e:
            logger.error(f"Error getting processes: {e}")
            raise ProcessError(str(e))
    
    @staticmethod
    def kill_process(pid):
        """
        Kill a process by PID.
        
        Args:
            pid (int): Process ID
            
        Returns:
            bool: True if successful
        """
        try:
            process = psutil.Process(pid)
            process.kill()
            logger.info(f"Killed process {pid}: {process.name()}")
            return True
        except psutil.NoSuchProcess:
            logger.error(f"Process not found: {pid}")
            raise ProcessError(f"Process {pid} not found")
        except Exception as e:
            logger.error(f"Error killing process {pid}: {e}")
            raise ProcessError(str(e))
    
    @staticmethod
    def force_kill_process(pid):
        """
        Force kill a process.
        
        Args:
            pid (int): Process ID
            
        Returns:
            bool: True if successful
        """
        try:
            result = subprocess.run(
                ["taskkill", "/PID", str(pid), "/F"],
                capture_output=True,
                check=False
            )
            
            if result.returncode == 0:
                logger.info(f"Force killed process {pid}")
                return True
            else:
                logger.error(f"Error force killing process: {result.stderr}")
                raise ProcessError(f"Failed to kill process {pid}")
        except Exception as e:
            logger.error(f"Exception force killing process: {e}")
            raise ProcessError(str(e))

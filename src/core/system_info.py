"""System information gathering module"""

import platform
import psutil
import subprocess
from utils.logger import Logger

logger = Logger("SystemInfo")

class SystemInfoGatherer:
    """
    Gathers system information for the dashboard.
    """
    
    @staticmethod
    def get_os_info():
        """
        Get operating system information.
        
        Returns:
            dict: OS information
        """
        try:
            return {
                "os": platform.system(),
                "version": platform.release(),
                "build": platform.version(),
                "architecture": platform.machine(),
                "hostname": platform.node(),
            }
        except Exception as e:
            logger.error(f"Error getting OS info: {e}")
            return {}
    
    @staticmethod
    def get_cpu_info():
        """
        Get CPU information and usage.
        
        Returns:
            dict: CPU information
        """
        try:
            return {
                "physical_cores": psutil.cpu_count(logical=False),
                "total_cores": psutil.cpu_count(logical=True),
                "usage_percent": psutil.cpu_percent(interval=1),
                "frequency_mhz": psutil.cpu_freq().current,
            }
        except Exception as e:
            logger.error(f"Error getting CPU info: {e}")
            return {}
    
    @staticmethod
    def get_memory_info():
        """
        Get memory information and usage.
        
        Returns:
            dict: Memory information
        """
        try:
            virtual_memory = psutil.virtual_memory()
            swap_memory = psutil.swap_memory()
            
            return {
                "total_gb": virtual_memory.total / (1024**3),
                "available_gb": virtual_memory.available / (1024**3),
                "used_gb": virtual_memory.used / (1024**3),
                "usage_percent": virtual_memory.percent,
                "swap_total_gb": swap_memory.total / (1024**3),
                "swap_used_gb": swap_memory.used / (1024**3),
                "swap_percent": swap_memory.percent,
            }
        except Exception as e:
            logger.error(f"Error getting memory info: {e}")
            return {}
    
    @staticmethod
    def get_disk_info():
        """
        Get disk information for all partitions.
        
        Returns:
            dict: Disk information
        """
        try:
            disks = {}
            for partition in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    disks[partition.device] = {
                        "mountpoint": partition.mountpoint,
                        "total_gb": usage.total / (1024**3),
                        "used_gb": usage.used / (1024**3),
                        "free_gb": usage.free / (1024**3),
                        "usage_percent": usage.percent,
                    }
                except PermissionError:
                    pass
            return disks
        except Exception as e:
            logger.error(f"Error getting disk info: {e}")
            return {}
    
    @staticmethod
    def get_network_info():
        """
        Get network information.
        
        Returns:
            dict: Network information
        """
        try:
            net_io = psutil.net_io_counters()
            return {
                "bytes_sent": net_io.bytes_sent,
                "bytes_recv": net_io.bytes_recv,
                "packets_sent": net_io.packets_sent,
                "packets_recv": net_io.packets_recv,
                "errors_in": net_io.errin,
                "errors_out": net_io.errout,
            }
        except Exception as e:
            logger.error(f"Error getting network info: {e}")
            return {}
    
    @staticmethod
    def get_uptime():
        """
        Get system uptime.
        
        Returns:
            str: Formatted uptime string
        """
        try:
            boot_time = psutil.boot_time()
            from datetime import datetime
            uptime_seconds = datetime.now().timestamp() - boot_time
            
            days = int(uptime_seconds // 86400)
            hours = int((uptime_seconds % 86400) // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            
            return f"{days}d {hours}h {minutes}m"
        except Exception as e:
            logger.error(f"Error getting uptime: {e}")
            return "N/A"

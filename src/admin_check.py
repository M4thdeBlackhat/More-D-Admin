"""Admin permission checker and UAC elevation handler"""

import ctypes
import sys
import os
import subprocess
from utils.logger import Logger

logger = Logger("AdminCheck")

def is_admin():
    """
    Check if the current process has administrator privileges.
    
    Returns:
        bool: True if admin, False otherwise
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        logger.error(f"Error checking admin status: {e}")
        return False

def request_admin_privileges():
    """
    Request administrator privileges by restarting the application with UAC elevation.
    
    Returns:
        bool: True if elevation was successful, False otherwise
    """
    try:
        if not is_admin():
            # Re-run the program with admin rights
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
            sys.exit()
    except Exception as e:
        logger.error(f"Error requesting admin privileges: {e}")
        return False
    return True

def check_and_elevate():
    """
    Check admin status and elevate if necessary.
    This should be called at application startup.
    """
    if not is_admin():
        logger.warning("Administrator privileges required. Requesting elevation...")
        request_admin_privileges()
        return False
    else:
        logger.info("Running with administrator privileges")
        return True

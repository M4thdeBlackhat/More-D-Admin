"""
Configuration file for More-D-Admin application
"""

# Application Settings
APP_NAME = "More-D-Admin"
APP_VERSION = "1.0.0"
APP_AUTHOR = "M4thdeBlackhat"

# Window Settings
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900
WINDOW_MIN_WIDTH = 1000
WINDOW_MIN_HEIGHT = 700

# Theme Settings
THEME_NAME = "dark"
PRIMARY_COLOR = "#1a1a1a"  # Dark background
ACCENT_COLOR = "#dc2626"   # Red accent
TEXT_COLOR = "#ffffff"      # White text
SECONDARY_COLOR = "#2a2a2a" # Slightly lighter dark

# Logging Settings
LOGS_DIR = "logs"
LOG_FILE = "more_d_admin.log"
LOG_LEVEL = "INFO"

# Backup Settings
BACKUP_DIR = "backups"
AUTO_BACKUP = True
AUTO_BACKUP_INTERVAL = 3600  # seconds

# UI Settings
SIDEBAR_WIDTH = 250
ICON_SIZE = 24
FONT_FAMILY = "Segoe UI"
FONT_SIZE_TITLE = 24
FONT_SIZE_HEADING = 18
FONT_SIZE_BODY = 12

# Security Settings
CONFIRM_DESTRUCTIVE_ACTIONS = True
AUTO_RESTORE_POINT = True
CRITICAL_FILES = [
    "C:\\Windows\\System32",
    "C:\\Windows\\SysWOW64",
    "C:\\Program Files",
    "C:\\Program Files (x86)",
]

# Feature Toggles
ENABLE_SERVICE_MANAGER = True
ENABLE_APP_MANAGER = True
ENABLE_FILE_TOOLS = True
ENABLE_REGISTRY_TOOLS = True
ENABLE_PROCESS_MANAGER = True
ENABLE_STARTUP_MANAGER = True
ENABLE_CLEANUP = True
ENABLE_DEFENDER_TOGGLE = True
ENABLE_OPTIMIZATION = True
ENABLE_SYSTEM_INFO = True

# Windows Services to display
MONITORED_SERVICES = [
    "Windows Update",
    "Windows Defender",
    "Superfetch",
    "Print Spooler",
    "Remote Desktop",
    "Bluetooth",
]

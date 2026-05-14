"""Main application entry point for More-D-Admin"""

import sys
import os
import customtkinter as ctk
from admin_check import check_and_elevate
from ui.main_window import MainWindow
from utils.logger import Logger
import config

logger = Logger("Main")

def main():
    """
    Main application entry point.
    """
    try:
        # Check and elevate to admin if needed
        if not check_and_elevate():
            sys.exit(1)
        
        logger.info(f"Starting {config.APP_NAME} v{config.APP_VERSION}")
        
        # Create root window
        root = ctk.CTk()
        root.title(config.APP_NAME)
        root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        root.minsize(config.WINDOW_MIN_WIDTH, config.WINDOW_MIN_HEIGHT)
        
        # Set appearance mode
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        # Create main window
        app = MainWindow(root)
        
        logger.info("Application started successfully")
        root.mainloop()
        
    except Exception as e:
        logger.critical(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()

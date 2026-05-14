"""Main application window"""

import customtkinter as ctk
from ui.sidebar import Sidebar
from ui.dashboard import Dashboard
from ui.services import ServicesTab
from ui.applications import ApplicationsTab
from ui.file_tools import FileToolsTab
from ui.registry import RegistryTab
from ui.process_manager import ProcessManagerTab
from ui.startup_manager import StartupManagerTab
from ui.cleanup import CleanupTab
from ui.defender import DefenderTab
from ui.optimization import OptimizationTab
from ui.logs import LogsTab
from utils.logger import Logger
import config

logger = Logger("MainWindow")

class MainWindow:
    """
    Main application window container.
    """
    
    def __init__(self, root):
        """
        Initialize main window.
        
        Args:
            root: CTk root window
        """
        self.root = root
        self.root.configure(fg_color="#1a1a1a")
        
        # Create main layout
        self.create_layout()
        
        # Track current tab
        self.current_tab = None
        self.tabs = {}
        
        logger.info("Main window initialized")
    
    def create_layout(self):
        """
        Create main layout with sidebar and content area.
        """
        # Main container
        main_container = ctk.CTkFrame(self.root, fg_color="#1a1a1a")
        main_container.pack(fill="both", expand=True)
        
        # Sidebar
        self.sidebar = Sidebar(main_container, self.switch_tab)
        self.sidebar.pack(side="left", fill="y", padx=0, pady=0)
        
        # Content area
        self.content_frame = ctk.CTkFrame(main_container, fg_color="#1a1a1a")
        self.content_frame.pack(side="right", fill="both", expand=True)
        
        # Initialize tabs
        self.initialize_tabs()
        
        # Show dashboard by default
        self.switch_tab("Dashboard")
    
    def initialize_tabs(self):
        """
        Initialize all application tabs.
        """
        self.tabs = {
            "Dashboard": Dashboard(self.content_frame),
            "Services": ServicesTab(self.content_frame),
            "Applications": ApplicationsTab(self.content_frame),
            "File Tools": FileToolsTab(self.content_frame),
            "Registry": RegistryTab(self.content_frame),
            "Processes": ProcessManagerTab(self.content_frame),
            "Startup": StartupManagerTab(self.content_frame),
            "Cleanup": CleanupTab(self.content_frame),
            "Defender": DefenderTab(self.content_frame),
            "Optimization": OptimizationTab(self.content_frame),
            "Logs": LogsTab(self.content_frame),
        }
    
    def switch_tab(self, tab_name):
        """
        Switch to a different tab.
        
        Args:
            tab_name (str): Name of the tab to switch to
        """
        try:
            # Hide current tab
            if self.current_tab:
                self.tabs[self.current_tab].pack_forget()
            
            # Show new tab
            self.tabs[tab_name].pack(fill="both", expand=True)
            self.current_tab = tab_name
            
            logger.info(f"Switched to tab: {tab_name}")
        except Exception as e:
            logger.error(f"Error switching to tab {tab_name}: {e}")

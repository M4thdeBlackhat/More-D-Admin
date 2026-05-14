"""Dashboard tab"""

import customtkinter as ctk
from ui.styles import AppTheme
from core.system_info import SystemInfoGatherer
from utils.logger import Logger

logger = Logger("Dashboard")

class Dashboard:
    """
    System information dashboard.
    """
    
    def __init__(self, parent):
        """
        Initialize dashboard.
        
        Args:
            parent: Parent widget
        """
        self.parent = parent
        self.frame = ctk.CTkFrame(parent, fg_color=AppTheme.PRIMARY_BG)
        self.create_widgets()
    
    def create_widgets(self):
        """
        Create dashboard widgets.
        """
        # Title
        title = ctk.CTkLabel(
            self.frame,
            text="System Dashboard",
            font=AppTheme.FONT_TITLE,
            text_color=AppTheme.TEXT_PRIMARY
        )
        title.pack(pady=20, padx=20, anchor="w")
        
        # Scrollable frame for content
        scroll_frame = ctk.CTkScrollableFrame(
            self.frame,
            fg_color=AppTheme.PRIMARY_BG
        )
        scroll_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Get system information
        self.update_system_info(scroll_frame)
    
    def update_system_info(self, parent):
        """
        Update and display system information.
        
        Args:
            parent: Parent widget
        """
        try:
            gatherer = SystemInfoGatherer()
            
            # OS Info
            os_info = gatherer.get_os_info()
            self.create_info_section(parent, "Operating System", os_info)
            
            # CPU Info
            cpu_info = gatherer.get_cpu_info()
            self.create_info_section(parent, "Processor", cpu_info)
            
            # Memory Info
            memory_info = gatherer.get_memory_info()
            self.create_info_section(parent, "Memory", memory_info)
            
            # Disk Info
            disk_info = gatherer.get_disk_info()
            self.create_info_section(parent, "Disk", disk_info)
            
            # Uptime
            uptime = gatherer.get_uptime()
            self.create_info_section(parent, "System Uptime", {"Uptime": uptime})
            
        except Exception as e:
            logger.error(f"Error updating system info: {e}")
            error_label = ctk.CTkLabel(
                parent,
                text=f"Error loading system information: {e}",
                text_color=AppTheme.ERROR_COLOR
            )
            error_label.pack(pady=10)
    
    def create_info_section(self, parent, title, info_dict):
        """
        Create an information section.
        
        Args:
            parent: Parent widget
            title (str): Section title
            info_dict (dict): Information to display
        """
        section_frame = ctk.CTkFrame(
            parent,
            fg_color=AppTheme.SECONDARY_BG,
            corner_radius=AppTheme.RADIUS_LG
        )
        section_frame.pack(fill="x", pady=10)
        
        # Section title
        title_label = ctk.CTkLabel(
            section_frame,
            text=title,
            font=AppTheme.FONT_HEADING,
            text_color=AppTheme.ACCENT_COLOR
        )
        title_label.pack(pady=10, padx=15, anchor="w")
        
        # Information items
        for key, value in info_dict.items():
            item_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
            item_frame.pack(fill="x", padx=15, pady=5)
            
            key_label = ctk.CTkLabel(
                item_frame,
                text=f"{key}:",
                font=AppTheme.FONT_BODY,
                text_color=AppTheme.TEXT_SECONDARY,
                width=200
            )
            key_label.pack(side="left", anchor="w")
            
            # Format value
            if isinstance(value, float):
                value_str = f"{value:.2f}"
            else:
                value_str = str(value)
            
            value_label = ctk.CTkLabel(
                item_frame,
                text=value_str,
                font=AppTheme.FONT_BODY,
                text_color=AppTheme.TEXT_PRIMARY
            )
            value_label.pack(side="left", anchor="w")
    
    def pack(self, **kwargs):
        """Pack the dashboard frame."""
        self.frame.pack(**kwargs)
    
    def pack_forget(self):
        """Unpack the dashboard frame."""
        self.frame.pack_forget()

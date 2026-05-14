"""Sidebar navigation component"""

import customtkinter as ctk
from ui.styles import AppTheme, UIConstants
from utils.logger import Logger

logger = Logger("Sidebar")

class Sidebar:
    """
    Sidebar navigation component.
    """
    
    def __init__(self, parent, callback):
        """
        Initialize sidebar.
        
        Args:
            parent: Parent widget
            callback: Callback function for tab switching
        """
        self.parent = parent
        self.callback = callback
        self.selected_button = None
        
        self.frame = ctk.CTkFrame(
            parent,
            width=UIConstants.SIDEBAR_WIDTH,
            fg_color=AppTheme.PRIMARY_BG
        )
        
        self.create_widgets()
    
    def create_widgets(self):
        """
        Create sidebar widgets.
        """
        # Header
        header = ctk.CTkLabel(
            self.frame,
            text="More-D-Admin",
            font=AppTheme.FONT_HEADING,
            text_color=AppTheme.ACCENT_COLOR
        )
        header.pack(pady=20, padx=10)
        
        # Divider
        divider = ctk.CTkFrame(
            self.frame,
            height=1,
            fg_color=AppTheme.BORDER_COLOR
        )
        divider.pack(fill="x", padx=10, pady=10)
        
        # Menu items
        menu_items = [
            ("📊 Dashboard", "Dashboard"),
            ("⚙️ Services", "Services"),
            ("📦 Applications", "Applications"),
            ("📁 File Tools", "File Tools"),
            ("🔧 Registry", "Registry"),
            ("⚡ Processes", "Processes"),
            ("🚀 Startup", "Startup"),
            ("🧹 Cleanup", "Cleanup"),
            ("🛡️ Defender", "Defender"),
            ("⚡ Optimization", "Optimization"),
            ("📋 Logs", "Logs"),
        ]
        
        for label, tab_name in menu_items:
            self.create_menu_button(label, tab_name)
    
    def create_menu_button(self, label, tab_name):
        """
        Create a menu button.
        
        Args:
            label (str): Button label
            tab_name (str): Associated tab name
        """
        button = ctk.CTkButton(
            self.frame,
            text=label,
            fg_color=AppTheme.SECONDARY_BG,
            hover_color=AppTheme.ACCENT_COLOR,
            text_color=AppTheme.TEXT_PRIMARY,
            font=AppTheme.FONT_BODY,
            corner_radius=AppTheme.RADIUS_MD,
            command=lambda: self.on_button_click(button, tab_name),
            anchor="w",
            width=UIConstants.SIDEBAR_WIDTH - 20
        )
        button.pack(pady=5, padx=10)
    
    def on_button_click(self, button, tab_name):
        """
        Handle button click.
        
        Args:
            button: Clicked button
            tab_name (str): Associated tab name
        """
        # Reset previous selection
        if self.selected_button:
            self.selected_button.configure(fg_color=AppTheme.SECONDARY_BG)
        
        # Highlight current selection
        button.configure(fg_color=AppTheme.ACCENT_COLOR)
        self.selected_button = button
        
        # Call callback
        self.callback(tab_name)
    
    def pack(self, **kwargs):
        """Pack the sidebar frame."""
        self.frame.pack(**kwargs)
    
    def pack_forget(self):
        """Unpack the sidebar frame."""
        self.frame.pack_forget()

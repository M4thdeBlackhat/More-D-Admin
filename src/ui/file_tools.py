"""Registry tools tab placeholder"""

import customtkinter as ctk
from ui.styles import AppTheme

class RegistryTab:
    """
    Registry tools tab.
    """
    
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(parent, fg_color=AppTheme.PRIMARY_BG)
        self.create_widgets()
    
    def create_widgets(self):
        label = ctk.CTkLabel(
            self.frame,
            text="Registry Tools",
            font=AppTheme.FONT_TITLE,
            text_color=AppTheme.TEXT_PRIMARY
        )
        label.pack(pady=20, padx=20)
    
    def pack(self, **kwargs):
        self.frame.pack(**kwargs)
    
    def pack_forget(self):
        self.frame.pack_forget()

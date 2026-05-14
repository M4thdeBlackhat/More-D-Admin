"""UI styling and themes for More-D-Admin"""

import config

class AppTheme:
    """
    Application theme configuration.
    """
    
    # Colors
    PRIMARY_BG = config.PRIMARY_COLOR          # #1a1a1a
    SECONDARY_BG = config.SECONDARY_COLOR      # #2a2a2a
    ACCENT_COLOR = config.ACCENT_COLOR         # #dc2626 (Red)
    TEXT_PRIMARY = config.TEXT_COLOR            # #ffffff
    TEXT_SECONDARY = "#b0b0b0"                 # Light gray
    BORDER_COLOR = "#3a3a3a"                   # Dark gray
    SUCCESS_COLOR = "#10b981"                  # Green
    WARNING_COLOR = "#f59e0b"                  # Amber
    ERROR_COLOR = "#ef4444"                    # Red
    INFO_COLOR = "#3b82f6"                     # Blue
    
    # Padding/Spacing
    PADDING_SM = 5
    PADDING_MD = 10
    PADDING_LG = 15
    PADDING_XL = 20
    
    # Border Radius
    RADIUS_SM = 4
    RADIUS_MD = 8
    RADIUS_LG = 12
    
    # Fonts
    FONT_TITLE = (config.FONT_FAMILY, config.FONT_SIZE_TITLE, "bold")
    FONT_HEADING = (config.FONT_FAMILY, config.FONT_SIZE_HEADING, "bold")
    FONT_BODY = (config.FONT_FAMILY, config.FONT_SIZE_BODY)
    FONT_SMALL = (config.FONT_FAMILY, 10)
    
    # Animations
    ANIMATION_SPEED = 300  # milliseconds
    HOVER_OPACITY = 0.8

class UIConstants:
    """
    UI constants and default values.
    """
    
    SIDEBAR_WIDTH = config.SIDEBAR_WIDTH
    ICON_SIZE = config.ICON_SIZE
    MIN_WINDOW_WIDTH = config.WINDOW_MIN_WIDTH
    MIN_WINDOW_HEIGHT = config.WINDOW_MIN_HEIGHT
    DEFAULT_WINDOW_WIDTH = config.WINDOW_WIDTH
    DEFAULT_WINDOW_HEIGHT = config.WINDOW_HEIGHT
    
    # Button sizes
    BUTTON_HEIGHT = 40
    BUTTON_WIDTH = 120
    SMALL_BUTTON_HEIGHT = 30
    SMALL_BUTTON_WIDTH = 80
    
    # Dialog sizes
    DIALOG_WIDTH = 500
    DIALOG_HEIGHT = 300
    CONFIRMATION_DIALOG_WIDTH = 400
    CONFIRMATION_DIALOG_HEIGHT = 200

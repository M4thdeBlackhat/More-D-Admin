# More-D-Admin

A professional open-source Windows 11 desktop utility for system administration tasks with a modern dark UI.

## Features

### Core Features
- Request administrator permissions on startup
- Enable/disable Windows services
- Take ownership of files and folders
- Unlock protected files before deletion
- Remove installed applications
- Startup app manager
- Temporary file cleaner
- Registry tools section
- Process manager with force close
- File permission editor
- System information dashboard
- Restore point creation before major actions
- Action logs/history panel

### Advanced Features
- Toggle Windows Defender real-time protection
- Toggle Windows Update services
- Windows optimization mode
- Hidden file visibility toggle
- One-click cache cleanup
- Batch operations support
- Search bar for apps/services/files
- Multi-tab layout

### Security & Stability
- Confirmation prompts before destructive actions
- Undo/recovery options where possible
- Prevention of critical Windows system file deletion
- Crash handling and error logging
- System restore point creation before major changes

## Requirements

- Windows 10/11
- Python 3.10+
- Administrator privileges
- CustomTkinter for UI
- PyInstaller for building .exe

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python src/main.py
```

## Building the .exe

```bash
python build.py
```

Or manually with PyInstaller:

```bash
pyinstaller --onefile --windowed --icon=assets/icon.ico --add-data "assets:assets" src/main.py
```

## Project Structure

```
More-D-Admin/
├── src/
│   ├── main.py                 # Application entry point
│   ├── admin_check.py          # Admin permission handler
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_window.py      # Main window setup
│   │   ├── sidebar.py          # Sidebar navigation
│   │   ├── dashboard.py        # System info dashboard
│   │   ├── services.py         # Services management UI
│   │   ├── applications.py     # App removal UI
│   │   ├── file_tools.py       # File ownership/permissions
│   │   ├── registry.py         # Registry editor UI
│   │   ├── process_manager.py  # Process manager UI
│   │   ├── startup_manager.py  # Startup apps UI
│   │   ├── cleanup.py          # Temp file cleaner UI
│   │   ├── defender.py         # Windows Defender toggle
│   │   ├── optimization.py     # System optimization UI
│   │   ├── logs.py             # Action history UI
│   │   └── styles.py           # UI theme and styling
│   ├── core/
│   │   ├── __init__.py
│   │   ├── service_manager.py  # Windows service operations
│   │   ├── file_operations.py  # File/folder operations
│   │   ├── registry_ops.py     # Registry operations
│   │   ├── process_ops.py      # Process management
│   │   ├── app_manager.py      # Application operations
│   │   ├── cleanup_ops.py      # Cleanup operations
│   │   ├── system_info.py      # System information gathering
│   │   ├── defender_manager.py # Defender operations
│   │   └── optimizer.py        # System optimization
│   └── utils/
│       ├── __init__.py
│       ├── logger.py           # Logging system
│       ├── errors.py           # Custom exceptions
│       ├── restore_point.py    # Restore point creation
│       └── backup.py           # Backup/undo operations
├── assets/
│   ├── icon.ico                # Application icon
│   ├── icon.png                # Application logo
│   └── themes/
│       └── dark_red.json       # Custom theme file
├── requirements.txt            # Python dependencies
├── build.py                    # Build script
├── config.py                   # Application configuration
└── .gitignore

```

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

M4thdeBlackhat

## Safety Notice

This application performs system-level operations. Always create a system restore point before using major features. Some operations require administrator privileges.

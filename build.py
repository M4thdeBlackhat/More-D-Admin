"""Build script for creating standalone .exe using PyInstaller"""

import os
import subprocess
import sys

def build_exe():
    """
    Build standalone .exe using PyInstaller.
    """
    print("More-D-Admin Build Script")
    print("=" * 50)
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Build command
    build_command = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=More-D-Admin",
        "--icon=assets/icon.ico" if os.path.exists("assets/icon.ico") else "",
        "--add-data=src:src",
        "--add-data=assets:assets",
        "--clean",
        "src/main.py"
    ]
    
    # Remove empty strings
    build_command = [cmd for cmd in build_command if cmd]
    
    print(f"Building executable...")
    print(f"Command: {' '.join(build_command)}")
    print()
    
    try:
        result = subprocess.run(build_command, check=True)
        
        if result.returncode == 0:
            print("\n" + "=" * 50)
            print("Build successful!")
            print("=" * 50)
            print("\nExecutable location: ./dist/More-D-Admin.exe")
            print("\nYou can now run More-D-Admin.exe directly!")
        else:
            print("\nBuild failed!")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"\nBuild error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_exe()

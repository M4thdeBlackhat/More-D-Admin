#!/usr/bin/env python
"""Quick start script for More-D-Admin"""

import subprocess
import sys
import os

def main():
    """
    Quick start script.
    """
    print("More-D-Admin Quick Start")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 10):
        print("Error: Python 3.10 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    
    # Install dependencies
    print("\n[1/3] Installing dependencies...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True
        )
        print("✓ Dependencies installed")
    except subprocess.CalledProcessError:
        print("✗ Failed to install dependencies")
        sys.exit(1)
    
    # Create necessary directories
    print("\n[2/3] Creating directories...")
    os.makedirs("logs", exist_ok=True)
    os.makedirs("backups", exist_ok=True)
    os.makedirs("assets", exist_ok=True)
    print("✓ Directories created")
    
    # Run application
    print("\n[3/3] Starting More-D-Admin...")
    print("=" * 50)
    print()
    
    try:
        subprocess.run([sys.executable, "src/main.py"], check=True)
    except KeyboardInterrupt:
        print("\n\nApplication stopped by user")
    except subprocess.CalledProcessError:
        print("\n✗ Error running application")
        sys.exit(1)

if __name__ == "__main__":
    main()

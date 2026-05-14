# Installation & Setup Guide

## Quick Start (Fastest Way)

### Option 1: Download & Run Pre-Built .exe (Easiest)

1. Go to the **Releases** section on GitHub
2. Download the latest `More-D-Admin.exe`
3. Right-click → Run as Administrator
4. Done! The app will start immediately

**No installation, no downloads, no configuration needed!**

---

## Option 2: Build from Source

If you want to build the .exe yourself or run from Python source:

### Prerequisites

- Windows 10/11
- Python 3.10 or higher ([Download Python](https://www.python.org/downloads/))
- Administrator privileges

### Step 1: Clone the Repository

```bash
git clone https://github.com/M4thdeBlackhat/More-D-Admin.git
cd More-D-Admin
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Directly from Python

```bash
python src/main.py
```

**Note:** The app will request administrator privileges automatically on first run.

### Step 4: Build Standalone .exe

If you want to create your own standalone executable:

```bash
python build.py
```

The .exe will be created in the `dist/` folder:

```
dist/More-D-Admin.exe
```

You can now run this .exe directly without Python installed!

---

## Option 3: Development Setup

If you want to contribute or modify the code:

### Prerequisites

- Git
- Python 3.10+
- Visual Studio Code (optional)

### Setup Steps

1. **Clone repository:**
   ```bash
   git clone https://github.com/M4thdeBlackhat/More-D-Admin.git
   cd More-D-Admin
   ```

2. **Create virtual environment (recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python src/main.py
   ```

5. **Make changes and test:**
   - Edit code in the `src/` directory
   - Run again to test changes

---

## Troubleshooting

### Issue: "Python not found" or "pip not found"

**Solution:** 
- Make sure Python is installed and added to PATH
- Restart your command prompt after installing Python
- Use `python -m pip install` instead of just `pip`

### Issue: Admin privileges not granted

**Solution:**
- Run the command prompt as Administrator
- Or double-click the .exe and select "Run as Administrator"

### Issue: CustomTkinter import error

**Solution:**
```bash
pip install --upgrade customtkinter
```

### Issue: PyInstaller not building the .exe

**Solution:**
```bash
pip install --upgrade pyinstaller
python build.py
```

### Issue: Missing assets or icon

**Solution:**
- Create an `assets/` folder in the root directory
- Add `icon.ico` if you have one (optional)
- The app will still run without assets

---

## System Requirements

- **OS:** Windows 10 or Windows 11
- **RAM:** 200 MB minimum (512 MB recommended)
- **Disk Space:** 50 MB for .exe, 100 MB for source
- **Admin Rights:** Required for most features

---

## First Run

When you run More-D-Admin for the first time:

1. **UAC Prompt:** Click "Yes" to allow admin privileges
2. **Logs Directory:** Automatically created in `./logs/`
3. **Backups:** Automatically created in `./backups/` when needed

---

## Next Steps

- Check the [README.md](README.md) for feature overview
- See [CONTRIBUTING.md](CONTRIBUTING.md) to help improve the project
- Report issues on [GitHub Issues](https://github.com/M4thdeBlackhat/More-D-Admin/issues)

---

## Support

For issues or questions:
1. Check existing [GitHub Issues](https://github.com/M4thdeBlackhat/More-D-Admin/issues)
2. Create a new issue with detailed information
3. Include your Windows version and error messages

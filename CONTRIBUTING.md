# Contributing to More-D-Admin

Thank you for your interest in contributing! This project is open-source and welcomes contributions from everyone.

## How to Contribute

### 1. Report Bugs

If you find a bug:

1. Check if it's already reported in [Issues](https://github.com/M4thdeBlackhat/More-D-Admin/issues)
2. Create a new issue with:
   - Clear title
   - Detailed description
   - Steps to reproduce
   - Your Windows version
   - Error messages/screenshots

### 2. Suggest Features

1. Create a new issue with "Feature Request" label
2. Explain the feature and why it would be useful
3. Provide examples if possible

### 3. Submit Code

#### Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/More-D-Admin.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Set up development environment: `pip install -r requirements.txt`

#### Development

1. Make your changes
2. Test thoroughly
3. Keep code style consistent with the project
4. Add comments for complex logic
5. Update documentation if needed

#### Commit & Push

```bash
# Make commits with clear messages
git commit -m "Add feature: description"

# Push to your fork
git push origin feature/your-feature-name
```

#### Create Pull Request

1. Go to the main repository
2. Click "New Pull Request"
3. Select your branch
4. Provide:
   - Clear title
   - Description of changes
   - Any related issues
   - Testing notes

### 4. Improve Documentation

Documentation improvements are always welcome:

- Fix typos
- Clarify instructions
- Add examples
- Translate to other languages

## Code Guidelines

### Style

- Follow PEP 8 Python style guide
- Use 4 spaces for indentation
- Use meaningful variable names
- Add docstrings to functions

### Example:

```python
def process_data(input_file, output_format="json"):
    """
    Process input data and convert to specified format.
    
    Args:
        input_file (str): Path to input file
        output_format (str): Output format (json, csv, xml)
        
    Returns:
        dict: Processed data
    """
    pass
```

### Logging

Use the logging system for all operations:

```python
from utils.logger import Logger

logger = Logger("ModuleName")
logger.info("Operation successful")
logger.error("Error occurred")
```

### Error Handling

Use custom exceptions from `utils/errors.py`:

```python
from utils.errors import FileOperationError

try:
    # operation
except Exception as e:
    logger.error(f"Error: {e}")
    raise FileOperationError(str(e))
```

## Project Structure

```
src/
├── main.py                 # Entry point
├── admin_check.py         # Admin privilege handling
├── ui/                    # User interface
│   ├── main_window.py    # Main window
│   ├── sidebar.py        # Navigation
│   ├── dashboard.py      # System info
│   └── [tabs].py         # Feature tabs
├── core/                  # Core functionality
│   ├── system_info.py    # System information
│   ├── service_manager.py
│   ├── file_operations.py
│   └── [other].py        # Other operations
└── utils/                 # Utilities
    ├── logger.py         # Logging
    ├── errors.py         # Exceptions
    ├── restore_point.py  # System restore
    └── backup.py         # Backup management
```

## Testing

Before submitting:

1. Test on Windows 10 and Windows 11
2. Test with and without admin privileges
3. Test error cases
4. Check logs for errors
5. Verify no data loss or system issues

## Commit Messages

Write clear commit messages:

```
# Good
git commit -m "Add service manager UI with start/stop functionality"

# Bad
git commit -m "update"
```

## Pull Request Process

1. Ensure all tests pass
2. Update documentation
3. Add yourself to CONTRIBUTORS.md
4. Await review
5. Address feedback
6. Merge!

## Questions?

Feel free to:
- Open a discussion issue
- Ask in pull request comments
- Check existing documentation

## License

By contributing, you agree your code will be released under the MIT License.

Thank you for contributing to More-D-Admin! 🎉

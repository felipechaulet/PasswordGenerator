# PasswordGenerator

Modern Python Password Generator with a sleek, minimalist interface.

## Features

- **Character Type Selection**: Choose from lowercase, uppercase, numbers, and special characters
- **Customizable Length**: Generate passwords from 4 to 30 characters
- **Modern UI**: Built with CustomTkinter for a contemporary look
- **Theme Support**: Light, dark, and system themes available
- **One-Click Copy**: Copy generated passwords to clipboard instantly
- **Menu Integration**: Access all functions through OS menu bar

## Interface

The application features:
- Minimalist icon-only buttons (🔄 Generate, 📋 Copy, ✕ Close)
- Compact checkbox options (abc, ABC, 123, !@#)
- Smooth password length slider
- Clean, modern design with rounded corners

## Requirements

- Python 3.8+
- customtkinter 5.2.2
- pyperclip 1.8.1

## Installation

1. Clone the repository:
```bash
git clone https://github.com/felipechaulet/PasswordGenerator.git
cd PasswordGenerator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python PasswordGenerator.py
```

## Contributing

We welcome contributions! Here's how to get started as a developer:

### Development Setup

1. **Fork and Clone**
```bash
git clone https://github.com/yourusername/PasswordGenerator.git
cd PasswordGenerator
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Install Development Tools** (Optional)
```bash
pip install black flake8 pytest
```

### Code Structure

- `PasswordGenerator.py` - Main application file containing the GUI and logic
- `requirements.txt` - Python dependencies
- `README.md` - Documentation

### Development Guidelines

1. **Code Style**
   - Follow PEP 8 conventions
   - Use meaningful variable names
   - Add comments for complex logic

2. **UI Guidelines**
   - Maintain minimalist design philosophy
   - Use icons where appropriate
   - Ensure responsive layout
   - Test on both light and dark themes

3. **Testing**
   - Test all character type combinations
   - Verify password length limits (4-30 characters)
   - Test clipboard functionality
   - Check theme switching

### Making Changes

1. **Create Feature Branch**
```bash
git checkout -b feature/your-feature-name
```

2. **Make Your Changes**
   - Keep commits focused and atomic
   - Write clear commit messages
   - Test your changes thoroughly

3. **Common Development Tasks**
   - **Adding new features**: Extend the `Application` class
   - **UI improvements**: Modify the `init_ui()` method
   - **Theme changes**: Update the `change_theme()` method
   - **Menu additions**: Modify the `create_menu()` method

4. **Test Your Changes**
```bash
python PasswordGenerator.py
```

5. **Submit Pull Request**
   - Push your branch to your fork
   - Create a pull request with clear description
   - Include screenshots for UI changes

### Architecture

The application uses:
- **CustomTkinter**: Modern UI framework
- **MVC Pattern**: Logic separated from presentation
- **Event-driven**: Button clicks and menu selections trigger actions
- **Cross-platform**: Works on Windows, macOS, and Linux

### Known Issues

- Password length is limited to 30 characters to fit in the display area
- Requires tkinter support (install `python-tk` on some systems)

## CI/CD Pipeline

This project uses GitHub Actions for automated testing and releases:

### Pull Request Workflow
- **Triggers**: New pull requests to `master`/`main` branch
- **Tests**: Runs on Ubuntu, Windows, and macOS with Python 3.8-3.12
- **Checks**:
  - Application import and basic functionality
  - Security scanning with Bandit
  - Code quality checks with Black and isort
  - Dependency vulnerability checks
- **Requirements**: All tests must pass before PR can be merged

### Release Workflow
- **Triggers**: Commits pushed to `master`/`main` branch
- **Process**:
  1. Creates a new GitHub release with auto-generated version
  2. Builds executable files for all platforms:
     - **Windows**: `PasswordGenerator-windows.exe`
     - **macOS**: `PasswordGenerator-macos.app.zip` 
     - **Linux**: `PasswordGenerator-linux`
  3. Uploads all executables to the release

### Download Releases
Visit the [Releases page](https://github.com/felipechaulet/PasswordGenerator/releases) to download the latest compiled version for your operating system.

### Branch Protection
- PRs require passing status checks
- Direct pushes to main branch trigger automatic releases
- All builds must succeed before release completion

### License

This project is open source. Feel free to contribute and improve it!
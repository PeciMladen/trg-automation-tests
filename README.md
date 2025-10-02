# TRG International - Automation Testing Framework

Automated testing framework for TRG International website using Python, Playwright, and Pytest with Page Object Model design pattern. Tests extract and validate Core Values from the Careers page.

---

## Quick Start

```bash
# Clone or download the repository
git clone https://github.com/pecimladen/trg-automation-tests.git
cd trg-automation-tests

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Run tests
pytest tests/test_core_values.py -v -s

# Generate HTML report
pytest tests/test_core_values.py --html=report.html --self-contained-html -s
```

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
  - [From Terminal](#from-terminal)
  - [From VS Code](#from-vs-code)
- [HTML Test Reports](#html-test-reports)
- [Project Structure](#project-structure)
- [Test Details](#test-details)
- [Expected Results](#expected-results)
- [Troubleshooting](#troubleshooting)
- [Resources](#resources)

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** ([Download](https://www.python.org/downloads/))
- **Git** (for cloning the repository) ([Download](https://git-scm.com/))
- **VS Code** (optional, but recommended for development) ([Download](https://code.visualstudio.com/))

**Verify Python installation:**
```bash
python --version
# or
python3 --version
```

---

## Installation

### Step 1: Clone the Repository

**Option A: Using Git (recommended)**
```bash
git clone https://github.com/pecimladen/trg-automation-tests.git
cd trg-automation-tests
```

**Option B: Download ZIP**
1. Go to the GitHub repository
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Navigate to the extracted folder in terminal

### Step 2: Create Virtual Environment

A virtual environment isolates project dependencies from your system Python installation.

```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` prefix in your terminal prompt.

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `pytest==8.0.0` - Testing framework
- `playwright==1.44.0` - Browser automation
- `pytest-playwright==0.4.4` - Pytest plugin for Playwright
- `requests==2.31.0` - HTTP library for downloading images
- `pytest-html==4.1.1` - HTML test report generation

### Step 5: Install Playwright Browser

```bash
playwright install chromium
```

This downloads Chromium browser (~100MB) used for automated testing.

### Step 6: Verify Installation

```bash
pytest --version
playwright --version
```

If both commands return version numbers, installation is successful.

---

## Running Tests

### From Terminal

#### Run All Tests
```bash
pytest
```

#### Run Specific Test File
```bash
# Core Values extraction test
pytest tests/test_core_values.py

# Random String generation test
pytest tests/test_random_string.py
```

#### Run with Verbose Output and Logs
```bash
# Verbose mode with detailed logs
pytest tests/test_core_values.py -v -s

# -v : verbose (shows test names)
# -s : shows print statements and logs in terminal
```

**Important:** Use the `-s` flag to see detailed execution logs in the terminal. Without it, output is captured and not displayed.

#### Run with Visible Browser (Headed Mode)
```bash
# By default, tests run in headless mode (no browser window)
# To see the browser during execution:
pytest tests/test_core_values.py --headed -s
```

#### Generate HTML Report
```bash
# Generate comprehensive HTML report with logs and screenshots
pytest tests/test_core_values.py --html=report.html --self-contained-html -s

# Open the report
# Windows:
start report.html

# macOS:
open report.html

# Linux:
xdg-open report.html
```

#### Other Useful Commands
```bash
# Stop on first failure
pytest -x

# Run last failed tests only
pytest --lf

# Run tests matching keyword
pytest -k "core_values"

# Show detailed test duration
pytest --durations=10
```

---

### From VS Code

#### Initial Setup (One-Time Configuration)

**1. Install Python Extension**
- Open VS Code
- Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac)
- Search for "Python" by Microsoft
- Click Install

**2. Select Python Interpreter**
- Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
- Type: `Python: Select Interpreter`
- Choose: `Python 3.x.x ('venv': venv)` from the list

**3. Configure Test Framework**
- Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
- Type: `Python: Configure Tests`
- Select `pytest`
- Select root directory (the project folder)

#### Method 1: Test Explorer (Recommended)

1. Click the Testing icon in the Activity Bar (beaker/flask icon)
2. Click "Refresh Tests" if needed
3. You'll see all tests in a tree structure
4. Click the play button (▶) next to any test to run it
5. Click the debug button (bug icon) to debug a test
6. View logs in the integrated terminal at the bottom

**Keyboard Shortcuts:**
- `Ctrl+; A` or `Cmd+; A` - Run all tests
- `Ctrl+; F` or `Cmd+; F` - Run tests in current file
- `Ctrl+; Ctrl+D` or `Cmd+; Cmd+D` - Debug last test

#### Method 2: Run and Debug Panel

**Create `.vscode/launch.json` in project root:**

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Pytest: All Tests",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": ["-v", "-s"],
            "console": "integratedTerminal",
            "justMyCode": false
        },
        {
            "name": "Pytest: Core Values Test",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": ["tests/test_core_values.py", "-v", "-s"],
            "console": "integratedTerminal",
            "justMyCode": false
        },
        {
            "name": "Pytest: With HTML Report",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": [
                "tests/test_core_values.py",
                "-v",
                "-s",
                "--html=report.html",
                "--self-contained-html"
            ],
            "console": "integratedTerminal",
            "justMyCode": false
        },
        {
            "name": "Pytest: Headed Mode (Visible Browser)",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": ["tests/test_core_values.py", "--headed", "-s"],
            "console": "integratedTerminal",
            "justMyCode": false
        }
    ]
}
```

**To run:**
1. Press `F5` or click Run → Start Debugging
2. Select configuration from dropdown menu
3. View output and logs in integrated terminal (View → Terminal or `` Ctrl+` ``)

#### Viewing Logs in VS Code Terminal

All test execution logs are displayed in the VS Code integrated terminal when using the `-s` flag. You'll see:
- Step-by-step execution logs
- Success/failure indicators
- Retry attempts
- Data extraction results
- Image download progress
- Error messages with details

**To open terminal in VS Code:**
- Menu: View → Terminal
- Keyboard: `` Ctrl+` `` (Windows/Linux) or `` Cmd+` `` (Mac)

---

## HTML Test Reports

The framework can generate HTML test reports using pytest-html plugin.

### Generating Reports

```bash
# Generate report
pytest tests/test_core_values.py --html=report.html --self-contained-html -s

# The --self-contained-html flag embeds all resources in a single file
# The -s flag ensures logs are captured
```

### Viewing Reports

The generated `report.html` file can be opened in any web browser:

```bash
# Windows
start report.html

# macOS
open report.html

# Linux
xdg-open report.html
```

The report includes:
- Test results (pass/fail status)
- Test duration
- Basic test information
- Links to test details

---

## Project Structure

```
trg-automation-tests/
│
├── .vscode/                    # VS Code configuration
│   └── launch.json            # Debug configurations (optional)
│
├── pages/                      # Page Object Models
│   ├── __init__.py
│   ├── base_page.py           # Base class with common methods
│   └── careers_page.py        # Careers page automation logic
│
├── tests/                      # Test files
│   ├── __init__.py
│   ├── test_core_values.py    # Core values extraction test
│   └── test_random_string.py  # String generator utility test
│
├── utils/                      # Utility functions
│   ├── __init__.py
│   └── string_generator.py    # Random string generator
│
├── data/                       # Test output (auto-generated)
│   ├── images/                # Downloaded core value images
│   │   ├── whatever-it-takes.png
│   │   ├── we-work-together.png
│   │   ├── we-make-an-impact.png
│   │   └── passion-is-our-fuel.png
│   └── core_values.json       # Extracted data with exclamation count
│
├── venv/                       # Virtual environment (not in git)
│
├── conftest.py                 # Pytest configuration and fixtures
├── pytest.ini                  # Pytest settings
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── report.html                 # HTML test report (generated after test run)
└── README.md                   # This file
```

---

## Test Details

### test_core_values.py

**Purpose:** Extracts Core Values from TRG International Careers page and validates data.

**Test Steps:**
1. Navigate to `https://www.trgint.com`
2. Accept cookies popup (if present)
3. Hover over "Who we are" menu to reveal dropdown
4. Click "Careers" link (opens in new tab)
5. Switch to Careers page tab
6. Navigate to "Life at TRG" section
7. Scroll to Core Values section
8. Extract 4 core values:
   - Headline (e.g., "Whatever it takes!")
   - Description (unique for each value)
9. Count total exclamation marks in all text
10. Download 4 core value images
11. Rename images based on their headlines
12. Save all data to JSON file

**Features:**
- 3 automatic retry attempts for reliability
- Handles cookie popups automatically
- Waits for page loads and animations
- Multiple fallback methods for data extraction
- Detailed logging at each step
- Screenshot on completion

**Expected Duration:** 60-90 seconds

### test_random_string.py

**Purpose:** Tests random string generation utility function.

**Test Cases:**
- Verifies string length is 10 characters
- Checks for presence of lowercase letters
- Checks for presence of uppercase letters
- Checks for presence of digits

**Expected Duration:** <1 second

---

## Expected Results

After running `pytest tests/test_core_values.py -v -s` successfully:

### Console Output

```
================================ test session starts =================================
TRG International - Test Automation Framework
Python + Playwright + Pytest with Page Object Model

   🔄 ATTEMPT 1/3
   → Step 1: Opening TRG main website...
   ✅ Loaded: https://www.trgint.com/
   
   → Step 2: Hovering over 'Who we are' menu...
   ✅ Hovering over 'Who we are'...
   → Waiting for dropdown menu to stabilize...
   ✅ Careers link is stable and ready
   
   → Step 3: Clicking 'Careers' link...
   → Trying to click: a:has-text('Careers')
   ✅ Clicked!
   ✅ Switched to: https://www.careers.trgint.com/
   ✅ Successfully on Careers page!
   
   → Extracting core values...
   ✓ Extracted core value 1: Whatever it takes!
   ✓ Extracted core value 2: We work together.
   ✓ Extracted core value 3: We make an impact.
   ✓ Extracted core value 4: Passion is our fuel.
   
   → Counting exclamation marks...
   ✅ Total exclamation marks: 2
   
   → Downloading core value images...
   ✓ Downloaded: whatever-it-takes.png
   ✓ Downloaded: we-work-together.png
   ✓ Downloaded: we-make-an-impact.png
   ✓ Downloaded: passion-is-our-fuel.png
   
================================= 1 passed in 68.37s =================================
```

### Generated Files

**1. `data/core_values.json`**
```json
{
  "core_values": [
    {
      "headline": "Whatever it takes!",
      "description": "We are always on the go. We follow a can-do approach..."
    },
    {
      "headline": "We work together.",
      "description": "One for all and all for one, embracing a culture..."
    },
    {
      "headline": "We make an impact.",
      "description": "We foster innovation and always ask why..."
    },
    {
      "headline": "Passion is our fuel.",
      "description": "We work with passion. We pursue growth..."
    }
  ],
  "exclamation_marks_count": 2,
  "total_values_extracted": 4
}
```

**2. `data/images/` - Four PNG files**
- `whatever-it-takes.png`
- `we-work-together.png`
- `we-make-an-impact.png`
- `passion-is-our-fuel.png`

**3. `report.html` - Comprehensive test report** (if generated with `--html` flag)

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'playwright'`

**Cause:** Virtual environment not activated or dependencies not installed.

**Solution:**
```bash
# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Verify activation (you should see (venv) in prompt)

# Reinstall dependencies
pip install -r requirements.txt
playwright install chromium
```

---

### Issue: `ImportError: cannot import name 'CareersPage'`

**Cause:** Missing `__init__.py` files or running from wrong directory.

**Solution:**
1. Verify you're in the project root directory:
   ```bash
   pwd  # Should show path ending in trg-automation-tests
   ```

2. Ensure `__init__.py` files exist:
   - `pages/__init__.py`
   - `tests/__init__.py`
   - `utils/__init__.py`

3. These should be empty files but must exist for Python to recognize directories as packages.

---

### Issue: Tests fail with "Could not click 'Careers' link"

**Cause:** Website structure changed, slow internet connection, or dropdown animation issues.

**Solution:**
1. Run in headed mode to see what's happening:
   ```bash
   pytest tests/test_core_values.py --headed -s
   ```

2. Check your internet connection

3. The test has 3 automatic retry attempts. If all fail:
   - Verify the website is accessible in a regular browser
   - Check if "Who we are" menu structure has changed
   - Wait a few minutes and try again (site might be slow)

---

### Issue: Images not downloading

**Cause:** Network issues, permissions, or missing folder.

**Solution:**
```bash
# Create data/images folder manually if needed
mkdir -p data/images  # macOS/Linux
md data\images        # Windows

# Check folder permissions
ls -la data/  # macOS/Linux
dir data\     # Windows

# Verify requests library is installed
pip list | grep requests

# Reinstall if needed
pip install requests
```

---

### Issue: VS Code doesn't detect tests

**Cause:** Test framework not configured or wrong interpreter selected.

**Solution:**
1. Open Command Palette: `Ctrl+Shift+P` / `Cmd+Shift+P`
2. Run: `Python: Select Interpreter`
3. Choose the interpreter with `('venv': venv)` in the name
4. Run: `Python: Configure Tests`
5. Select `pytest` → root directory
6. Reload window: `Developer: Reload Window`
7. Check Output panel → Python Test Log for errors

---

### Issue: Virtual environment activation fails on Windows

**Cause:** PowerShell execution policy restriction.

**Solution:**
```powershell
# Open PowerShell as Administrator
# Run this command:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Close and reopen terminal, then activate:
venv\Scripts\activate
```

---

### Issue: `playwright install` fails

**Cause:** Network issues, insufficient disk space, or permissions.

**Solution:**
```bash
# Install with verbose output to see what's happening
playwright install chromium --verbose

# Linux users may need system dependencies
sudo playwright install-deps

# Check available disk space (needs ~100MB)
df -h  # macOS/Linux
```

---

### Issue: HTML report not generated

**Cause:** Missing `--html` flag or pytest-html not installed.

**Solution:**
```bash
# Verify pytest-html is installed
pip list | grep pytest-html

# Install if missing
pip install pytest-html

# Generate report with correct flags
pytest tests/test_core_values.py --html=report.html --self-contained-html -s
```

---

## Resources

- [Playwright Python Documentation](https://playwright.dev/python/) - Official Playwright docs
- [Pytest Documentation](https://docs.pytest.org/) - Pytest testing framework
- [Page Object Model Pattern](https://playwright.dev/python/docs/pom) - Design pattern explanation
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html) - Virtual environment guide
- [pytest-html Documentation](https://pytest-html.readthedocs.io/) - HTML report plugin

---

## Project Information

**Framework:** Pytest + Playwright + Page Object Model  
**Language:** Python 3.8+  
**Browser:** Chromium (headless by default)  
**Design Pattern:** Page Object Model for maintainability  

**Key Features:**
- Automated retry mechanism (3 attempts)
- Comprehensive logging
- HTML report generation with screenshots
- Screenshot capture on test completion
- Configurable browser modes (headed/headless)
- Cookie popup handling
- Dynamic wait strategies
- Data extraction and validation
- Image downloading and renaming
- JSON output generation

---

**Happy Testing!**
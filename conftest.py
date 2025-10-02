"""
Pytest configuration and fixtures
"""
import pytest
import sys
from playwright.sync_api import sync_playwright
from pytest_html import extras


@pytest.fixture(scope="function")
def browser():
    """Create a browser instance for each test"""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=500
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """Create a new page for each test"""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )
    page = context.new_page()
    yield page
    page.close()
    context.close()


def pytest_configure(config):
    """Configure pytest with custom markers and metadata"""
    config.addinivalue_line(
        "markers", "core_values: Tests related to core values extraction"
    )
    config.addinivalue_line(
        "markers", "string_generator: Tests for random string generator"
    )
    
    # Add metadata for HTML report
    config._metadata = {
        'Project': 'TRG International - Automation Tests',
        'Test Framework': 'Pytest + Playwright',
        'Browser': 'Chromium',
        'Python Version': sys.version,
        'Playwright Mode': 'Headed (visible browser)'
    }


def pytest_report_header(config):
    """Display custom header when tests start"""
    return [
        "=" * 70,
        "TRG International - Test Automation Framework",
        "Python + Playwright + Pytest with Page Object Model",
        "=" * 70
    ]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to customize test reports
    Captures logs and screenshots for HTML report
    """
    outcome = yield
    report = outcome.get_result()
    
    # Initialize extras list for HTML report
    report.extras = getattr(report, 'extras', [])
    
    # Add logs and screenshots only during test execution (not setup/teardown)
    if report.when == 'call':
        
        # ===== CAPTURE LOGS =====
        # Capture stdout (print statements)
        if hasattr(report, 'capstdout') and report.capstdout:
            formatted_logs = format_logs_for_html(report.capstdout)
            report.extras.append(extras.html(formatted_logs))
        
        # Capture stderr (error messages)
        if hasattr(report, 'capstderr') and report.capstderr:
            report.extras.append(extras.text(report.capstderr, name="Error Output"))
        
        # ===== CAPTURE SCREENSHOT =====
        if hasattr(item, 'funcargs') and 'page' in item.funcargs:
            page = item.funcargs['page']
            try:
                # Take full page screenshot
                screenshot_bytes = page.screenshot(full_page=True)
                
                # Convert bytes to base64 string (required by pytest-html)
                import base64
                screenshot_base64 = base64.b64encode(screenshot_bytes).decode('utf-8')
                
                if report.failed:
                    # Red banner for failed tests
                    report.extras.append(extras.html('<h3 style="color: red;">❌ Test Failed - Screenshot:</h3>'))
                    report.extras.append(extras.image(screenshot_base64, name="Failure Screenshot"))
                else:
                    # Green banner for passed tests
                    report.extras.append(extras.html('<h3 style="color: green;">✅ Test Passed - Final Screenshot:</h3>'))
                    report.extras.append(extras.image(screenshot_base64, name="Success Screenshot"))
                    
            except Exception as e:
                # If screenshot fails, add note to report
                report.extras.append(extras.text(f"Could not capture screenshot: {str(e)}", name="Screenshot Error"))
    
    # ===== ADD TEST DURATION =====
    if hasattr(report, 'duration'):
        duration_html = f'<p style="font-size: 14px; margin-top: 10px;"><strong>⏱️ Test Duration:</strong> {report.duration:.2f} seconds</p>'
        report.extras.append(extras.html(duration_html))


def format_logs_for_html(logs):
    """
    Format console logs into HTML with color coding for better readability
    """
    html = '<div style="background-color: #1e1e1e; padding: 15px; border-radius: 8px; font-family: \'Courier New\', monospace; white-space: pre-wrap; max-height: 600px; overflow-y: auto; border: 2px solid #444;">'
    html += '<h4 style="margin-top: 0; color: #61dafb; border-bottom: 2px solid #61dafb; padding-bottom: 5px;">📋 Test Execution Logs:</h4>'
    
    # Split logs by line and format each line
    lines = logs.split('\n')
    for line in lines:
        if not line.strip():
            continue
        
        # Color code different log types based on emoji or keywords
        if '✅' in line or 'PASSED' in line or '✓' in line or 'Successfully' in line:
            color = '#28a745'  # Green - success
        elif '❌' in line or 'FAILED' in line or 'ERROR' in line or 'Error' in line:
            color = '#dc3545'  # Red - error
        elif '⚠️' in line or 'WARNING' in line or 'Could not' in line:
            color = '#ffc107'  # Yellow - warning
        elif '→' in line or 'Step' in line:
            color = '#007bff'  # Blue - step/action
        elif '🔄' in line or 'ATTEMPT' in line or 'Retry' in line:
            color = '#6f42c1'  # Purple - retry
        elif 'ℹ️' in line or 'INFO' in line:
            color = '#17a2b8'  # Cyan - info
        elif 'Extracted' in line or 'Downloaded' in line or 'Saved' in line:
            color = '#20c997'  # Teal - data operations
        elif 'Looking for' in line or 'Searching' in line or 'Checking' in line:
            color = '#fd7e14'  # Orange - search operations
        else:
            color = '#d4d4d4'  # Light gray - default
        
        # Add line with color
        html += f'<div style="color: {color}; margin: 3px 0; line-height: 1.5;">{line}</div>'
    
    html += '</div>'
    return html


@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    """
    Customize HTML report title
    """
    report.title = "TRG International - Automation Test Report"


def pytest_html_results_table_header(cells):
    """
    Customize HTML report table headers
    """
    cells.insert(2, '<th>Test Description</th>')
    cells.insert(3, '<th class="sortable time" data-column-type="time">Duration</th>')


def pytest_html_results_table_row(report, cells):
    """
    Customize HTML report table rows
    """
    # Add test description (full test path)
    cells.insert(2, f'<td style="font-size: 12px;">{report.nodeid}</td>')
    
    # Add duration with formatting
    if hasattr(report, 'duration'):
        duration = f'{report.duration:.2f}s'
        
        # Color code duration: green (<30s), yellow (30-60s), red (>60s)
        if report.duration < 30:
            color = '#28a745'
        elif report.duration < 60:
            color = '#ffc107'
        else:
            color = '#dc3545'
        
        cells.insert(3, f'<td class="col-duration" style="color: {color}; font-weight: bold;">{duration}</td>')
    else:
        cells.insert(3, '<td class="col-duration">-</td>')
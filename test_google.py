import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime


def pytest_configure(config):
    """Register custom markers to avoid warnings."""
    config.addinivalue_line("markers", "smoke: mark test as smoke test")
    config.addinivalue_line("markers", "priority_high: mark test as high priority")
    config.addinivalue_line("markers", "priority_medium: mark test as medium priority")
    config.addinivalue_line("markers", "priority_low: mark test as low priority")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to store test result in the node for access in fixtures."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture
def driver(request):
    """Pytest fixture to initialize and quit the WebDriver with screenshot capture on failure."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    yield driver
    
    # Capture screenshot on test failure
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"failure_{request.node.name}_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"\n❌ Test failed - Screenshot saved: {screenshot_path}")
    
    driver.quit()


@pytest.mark.smoke
@pytest.mark.priority_high
def test_google_homepage_title(driver):
    """Test to verify Google homepage title."""
    driver.get("https://www.google.com/")
    assert "Google" in driver.title
    print(f"✓ Page title verified: {driver.title}")


@pytest.mark.smoke
@pytest.mark.priority_medium
def test_google_homepage_loaded(driver):
    """Test to verify Google homepage loads successfully."""
    driver.get("https://www.google.com/")
    assert driver.current_url == "https://www.google.com/"
    print(f"✓ Page loaded successfully: {driver.current_url}")

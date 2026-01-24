import pytest


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

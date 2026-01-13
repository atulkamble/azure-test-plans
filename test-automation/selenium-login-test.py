"""
Selenium Test Automation for Azure Test Plans Demo
Tests the login functionality of the sample web application
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

class LoginTests:
    def __init__(self, base_url="http://localhost:8080"):
        self.base_url = base_url
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        self.test_results = []

    def log_result(self, test_name, passed, message=""):
        status = "✅ PASS" if passed else "❌ FAIL"
        result = f"{status}: {test_name}"
        if message:
            result += f" - {message}"
        print(result)
        self.test_results.append((test_name, passed, message))

    def test_valid_login(self):
        """Test Case: Verify login with valid credentials"""
        test_name = "Valid Login Test"
        try:
            print(f"\n🧪 Running: {test_name}")
            
            # Step 1: Open login page
            self.driver.get(self.base_url)
            time.sleep(1)
            assert "Login" in self.driver.title, "Login page did not load"
            
            # Step 2: Enter valid username
            username_field = self.driver.find_element(By.ID, "username")
            username_field.send_keys("admin")
            
            # Step 3: Enter valid password
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys("admin123")
            
            # Step 4: Click login button
            login_button = self.driver.find_element(By.ID, "login")
            login_button.click()
            time.sleep(2)
            
            # Verify dashboard is displayed
            assert "Dashboard" in self.driver.title, "Dashboard not displayed"
            
            # Verify welcome message
            welcome_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "welcomeUser"))
            )
            assert "admin" in welcome_element.text, "Welcome message not displayed correctly"
            
            self.log_result(test_name, True, "User successfully logged in")
            return True
            
        except Exception as e:
            self.log_result(test_name, False, str(e))
            return False

    def test_invalid_login(self):
        """Test Case: Verify login with invalid credentials"""
        test_name = "Invalid Login Test"
        try:
            print(f"\n🧪 Running: {test_name}")
            
            # Navigate to login page
            self.driver.get(self.base_url)
            time.sleep(1)
            
            # Enter invalid username
            username_field = self.driver.find_element(By.ID, "username")
            username_field.send_keys("user")
            
            # Enter invalid password
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys("wrongpass")
            
            # Click login button
            login_button = self.driver.find_element(By.ID, "login")
            login_button.click()
            time.sleep(2)
            
            # Verify error message is displayed
            error_message = self.driver.find_element(By.ID, "errorMessage")
            assert error_message.is_displayed(), "Error message not displayed"
            
            # Verify still on login page
            assert "Login" in self.driver.title, "User incorrectly logged in"
            
            self.log_result(test_name, True, "Error message displayed correctly")
            return True
            
        except Exception as e:
            self.log_result(test_name, False, str(e))
            return False

    def test_empty_credentials(self):
        """Test Case: Verify login with empty credentials"""
        test_name = "Empty Credentials Test"
        try:
            print(f"\n🧪 Running: {test_name}")
            
            # Navigate to login page
            self.driver.get(self.base_url)
            time.sleep(1)
            
            # Try to submit without entering credentials
            # HTML5 validation should prevent submission
            username_field = self.driver.find_element(By.ID, "username")
            is_required = username_field.get_attribute("required")
            
            assert is_required is not None, "Username field should be required"
            
            password_field = self.driver.find_element(By.ID, "password")
            is_required = password_field.get_attribute("required")
            
            assert is_required is not None, "Password field should be required"
            
            self.log_result(test_name, True, "Required validation working correctly")
            return True
            
        except Exception as e:
            self.log_result(test_name, False, str(e))
            return False

    def test_logout(self):
        """Test Case: Verify logout functionality"""
        test_name = "Logout Test"
        try:
            print(f"\n🧪 Running: {test_name}")
            
            # First login
            self.driver.get(self.base_url)
            time.sleep(1)
            
            self.driver.find_element(By.ID, "username").send_keys("admin")
            self.driver.find_element(By.ID, "password").send_keys("admin123")
            self.driver.find_element(By.ID, "login").click()
            time.sleep(2)
            
            # Verify on dashboard
            assert "Dashboard" in self.driver.title, "Not on dashboard"
            
            # Click logout
            logout_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "logout-button"))
            )
            logout_button.click()
            time.sleep(2)
            
            # Verify back on login page
            assert "Login" in self.driver.title, "Logout failed"
            
            # Verify form is cleared
            username_field = self.driver.find_element(By.ID, "username")
            assert username_field.get_attribute("value") == "", "Username field not cleared"
            
            self.log_result(test_name, True, "Logout successful")
            return True
            
        except Exception as e:
            self.log_result(test_name, False, str(e))
            return False

    def run_all_tests(self):
        """Run all test cases"""
        print("=" * 60)
        print("🚀 Azure Test Plans - Automated Test Execution")
        print("=" * 60)
        
        tests = [
            self.test_valid_login,
            self.test_invalid_login,
            self.test_empty_credentials,
            self.test_logout
        ]
        
        passed = 0
        failed = 0
        
        for test in tests:
            if test():
                passed += 1
            else:
                failed += 1
        
        print("\n" + "=" * 60)
        print("📊 Test Execution Summary")
        print("=" * 60)
        print(f"Total Tests: {len(tests)}")
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print(f"Success Rate: {(passed/len(tests)*100):.1f}%")
        print("=" * 60)
        
        return failed == 0

    def cleanup(self):
        """Close browser and cleanup"""
        self.driver.quit()


if __name__ == "__main__":
    # Check if custom URL provided
    base_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8080"
    
    test_suite = LoginTests(base_url)
    
    try:
        success = test_suite.run_all_tests()
        test_suite.cleanup()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Test execution failed: {e}")
        test_suite.cleanup()
        sys.exit(1)

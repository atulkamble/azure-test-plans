@echo off
echo 🧪 Azure Test Plans - Automated Test Execution
echo ==============================================
echo.

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python first.
    pause
    exit /b 1
)

echo ✅ Python found
echo.

if not exist "test-automation\venv" (
    echo 📦 Creating virtual environment...
    python -m venv test-automation\venv
    echo ✅ Virtual environment created
    echo.
)

echo 🔧 Activating virtual environment...
call test-automation\venv\Scripts\activate.bat

echo 📥 Installing test dependencies...
pip install -q --upgrade pip
pip install -q -r test-automation\requirements.txt
echo ✅ Dependencies installed
echo.

echo 🔍 Checking if application is running on port 8080...
curl -s http://localhost:8080 >nul 2>nul
if %errorlevel% neq 0 (
    echo ⚠️  Application is not running!
    echo Please start the application first using: run-app.bat
    echo.
    echo Or run in a separate terminal:
    echo    cd app ^&^& python -m http.server 8080
    call deactivate
    pause
    exit /b 1
)

echo ✅ Application is running
echo.

echo 🚀 Running Selenium tests...
echo.
cd test-automation
python selenium-login-test.py http://localhost:8080

set TEST_EXIT_CODE=%errorlevel%

call deactivate

echo.
if %TEST_EXIT_CODE% equ 0 (
    echo ✅ All tests passed!
) else (
    echo ❌ Some tests failed!
)

pause
exit /b %TEST_EXIT_CODE%

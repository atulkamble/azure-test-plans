@echo off
echo 🚀 Starting Azure Test Plans Demo Application
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

cd app

echo 📦 Starting HTTP server on port 8080...
echo.
echo ✅ Application is running!
echo 🌐 Open your browser and navigate to: http://localhost:8080
echo.
echo 📝 Test Credentials:
echo    Username: admin
echo    Password: admin123
echo.
echo Press Ctrl+C to stop the server
echo.

python -m http.server 8080

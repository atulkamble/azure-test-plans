#!/bin/bash

echo "🧪 Azure Test Plans - Automated Test Execution"
echo "=============================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "✅ Python 3 found"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "test-automation/venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv test-automation/venv
    echo "✅ Virtual environment created"
    echo ""
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source test-automation/venv/bin/activate

# Install dependencies
echo "📥 Installing test dependencies..."
pip install -q --upgrade pip
pip install -q -r test-automation/requirements.txt
echo "✅ Dependencies installed"
echo ""

# Check if application is running
echo "🔍 Checking if application is running on port 8080..."
if ! curl -s http://localhost:8080 > /dev/null; then
    echo "⚠️  Application is not running!"
    echo "Please start the application first using: ./run-app.sh"
    echo ""
    echo "Or run in a separate terminal:"
    echo "   cd app && python3 -m http.server 8080"
    deactivate
    exit 1
fi

echo "✅ Application is running"
echo ""

# Run tests
echo "🚀 Running Selenium tests..."
echo ""
cd test-automation
python selenium-login-test.py http://localhost:8080

# Capture exit code
TEST_EXIT_CODE=$?

# Deactivate virtual environment
deactivate

echo ""
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "✅ All tests passed!"
else
    echo "❌ Some tests failed!"
fi

exit $TEST_EXIT_CODE

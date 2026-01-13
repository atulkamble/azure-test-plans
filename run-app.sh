#!/bin/bash

echo "🚀 Starting Azure Test Plans Demo Application"
echo "=============================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "✅ Python 3 found"
echo ""

# Navigate to app directory
cd app

echo "📦 Starting HTTP server on port 8080..."
echo ""
echo "✅ Application is running!"
echo "🌐 Open your browser and navigate to: http://localhost:8080"
echo ""
echo "📝 Test Credentials:"
echo "   Username: admin"
echo "   Password: admin123"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start Python HTTP server
python3 -m http.server 8080

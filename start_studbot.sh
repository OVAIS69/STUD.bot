#!/bin/bash

echo "Starting StudBot AI Learning Companion..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.7+ from your package manager"
    exit 1
fi

# Check if requirements are installed
echo "Checking dependencies..."
if ! python3 -c "import flask" &> /dev/null; then
    echo "Installing required packages..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies"
        exit 1
    fi
fi

echo
echo "Starting Flask server..."
echo "StudBot will be available at: http://localhost:5000"
echo
echo "Press Ctrl+C to stop the server"
echo

# Start the Flask application
python3 app.py

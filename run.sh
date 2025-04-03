#!/bin/bash

echo "Set the DISPLAY variable for local host."
export DISPLAY=:0

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

#echo "Installing dependencies..."
# pip install -r requirements.txt

echo "Running the Application..."
python3 main.py
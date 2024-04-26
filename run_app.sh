#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 could not be found. Please install Python 3."
    exit
fi

# Navigate to the directory containing bhojanGPT.py and requirements.txt
cd "$(dirname "$0")"

# Check if requirements.txt exists in the current directory
if [ ! -f requirements.txt ]; then
    echo "requirements.txt not found in the current directory."
    exit 1
fi

# Install requirements
echo "Installing requirements from requirements.txt..."
pip3 install -q -r requirements.txt

# Check if installation was successful
if [ $? -ne 0 ]; then
    echo "Failed to install required packages. Please check the requirements file."
    exit 1
fi

# Run the Streamlit app
echo "Running Streamlit app..."
streamlit run bhojanGPT.py
#!/bin/sh

# GLOBALS
# -------

# Define ANSI color escape codes
ERROR='\033[0;31m'
SUCCESS='\033[0;32m'
INFO='\033[0;34m'
WARNING='\033[0;33m'
NC='\033[0m'  # No Color

# Define variables
PYTHON_PATH="/usr/bin/python3"
VENV_PATH="venv"


# FUNCTIONS
# ---------

# Function to deactivate and remove the virtual environment
deactivate_venv() {
    echo "${INFO}[INFO] Deactivating virtual env - ${VENV_PATH}..."
    echo "-----------------------------------------${NC}"
    if [ -n "$VIRTUAL_ENV" ]; then
        deactivate || true 
        echo "Virtual env deactivated: $VENV_PATH"
    else
        echo "Virtual env is not activated."
    fi
    rm -rf "$VENV_PATH"
    
    echo "\n${SUCCESS}[SUCCESS] Deactivation completed!${NC}"
}

# Function to create and activate the virtual environment, and install requirements
activate_venv() {
    echo "${INFO}[INFO] Creating virtual env ${VENV_PATH}..."
    echo "-------------------------------------------${NC}"
    if [ -n "$VIRTUAL_ENV" ]; then
        echo "Virtual env is already activated: $VENV_PATH"
    else
        $PYTHON_PATH -m venv $VENV_PATH
        . $VENV_PATH/bin/activate
        echo "Virtual env activated: $VENV_PATH"
    fi

    echo "\n${INFO}[INFO] Installing requirements..."
    echo "----------------------------------${NC}"
    python3 -m pip install --upgrade pip
    python3 -m pip install --force-reinstall -r requirements.txt

    echo "\n${INFO}[INFO] Installed packages:"
    echo "---------------------------${NC}"
    python3 -m pip freeze
    
    echo "\n${SUCCESS}[SUCCESS] Virtual env is ready!${NC}"
}


# SCRIPT
# ------

# Main script logic
if [ "$1" = "--activate" ] || [ $# -eq 0 ]; then
    if [ -n "$VIRTUAL_ENV" ]; then
        deactivate_venv
        activate_venv
    else
        activate_venv
    fi
elif [ "$1" = "--deactivate" ]; then
    deactivate_venv
else
    echo "${ERROR}[ERROR] Invalid argument: $1"
    echo "${INFO}[USAGE] source ./virtualenv.sh [--activate] [--deactivate]${NC}"
    echo "${INFO} - Use --activate or no argument to activate virtual env.${NC}"
    echo "${INFO} - Use --deactivate to deactivate virtual env.${NC}"
fi

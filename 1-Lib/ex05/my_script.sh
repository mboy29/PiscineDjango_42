#!/bin/sh


# GLOBALS
# -------

# Define ANSI color escape codes
ERROR='\033[0;31m'
SUCCESS='\033[0;32m'
INFO='\033[0;34m'
WARNING='\033[0;33m'
NC='\033[0m'

# Define variables
PYTHON_PATH="/usr/bin/python3"
VENV_PATH="django_venv"


# FUNCTIONS
# ---------

# Function to clean up files and directories
deactivate_venv() {
    echo "${INFO}[INFO] Deactivating virtual env - venv..."
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

# Function to activate virtual environment and install requirements
activate_venv() {
    echo "${INFO}[INFO] Creating virtual env ${VENV_PATH}..."
    echo "-------------------------------------------${NC}"
    if [ -n "$VIRTUAL_ENV" ]; then
        echo "Virtual env is already activated: $VENV_PATH"
    else
        $PYTHON_PATH -m virtualenv $VENV_PATH
        . $VENV_PATH/bin/activate
        echo "Virtual env activated: $VENV_PATH"

        echo "\n${INFO}[INFO] Installing requirements..."
        echo "----------------------------------${NC}"
        python3 -m pip install --force-reinstall -r requirement.txt
    fi
    echo "\n${SUCCESS}[SUCCESS] Virtual env is ready!${NC}"
}


# SCRIPT
# ------

# Main script logic
if [ "$1" = "--activate" ] || [ $# -eq 0 ]; then
    activate_venv
elif [ "$1" = "--deactivate" ]; then
    deactivate_venv
else
    echo "${ERROR}[ERROR] Invalid argument: $1"
    echo "${INFO}[USAGE] source ./my_script.sh [--activate] [--deactivate]${NC}"
    echo "${INFO} - Use --activate or no argument to activate virtual env.${NC}"
    echo "${INFO} - Use --deactivate to deactivate virtual env.${NC}"
fi

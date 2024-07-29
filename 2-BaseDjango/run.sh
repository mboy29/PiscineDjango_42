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
PYTHON_PATH="python3"
VENV_PATH="venv"


# FUNCTIONS
# ---------

# Function to clean up static files
clean() {
    echo "${INFO}[INFO] Cleaning up static files...${NC}"
    echo "-----------------------------------------"
    
    echo "${INFO}[INFO] Deleting collected static files...${NC}"
    rm -rf staticfiles/ 
    echo "Static files deleted."

    echo "\n${SUCCESS}[SUCCESS] Clean up completed!${NC}"
}

# Function to run migrations, collect static files, and start the server
run() {
    echo "${INFO}[INFO] Running migrations, collecting static files, and starting the server...${NC}"
    echo "---------------------------------------------------------"
    
    # Apply database migrations
    echo "${INFO}[INFO] Applying database migrations...${NC}"
    ${PYTHON_PATH} -B manage.py migrate
    
    # Collect static files
    echo "${INFO}[INFO] Collecting static files...${NC}"
    ${PYTHON_PATH} -B manage.py collectstatic --noinput
    
    # Start the Django development server
    echo "${INFO}[INFO] Starting the Django development server...${NC}"
    ${PYTHON_PATH} -B manage.py runserver
}


# SCRIPT
# ------

# Main script logic
if [ "$1" = "--run" ] || [ $# -eq 0 ]; then
    run
elif [ "$1" = "--clean" ]; then
    clean
else
    echo "${ERROR}[ERROR] Invalid argument: $1${NC}"
    echo "${INFO}[USAGE] ./run.sh [--run] [--clean]${NC}"
    echo "${INFO} - Use --run to run migrations, collect static files, and start the server.${NC}"
    echo "${INFO} - Use --clean to clean up static files.${NC}"
fi

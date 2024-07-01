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
LOG_PATH="pip_install.log"
PYTHON_PATH="/usr/bin/python3"
LIB_PATH="local_lib"

PATH_PY_URL="https://github.com/jaraco/path.git"
PROGRAM_PATH="my_program.py"
PROGRAM_EXAMPLE_PATH="example_folder"


# FUNCTIONS
# ---------

# Function to clean up files and directories
clean_up() {
    echo "${INFO}[INFO] Cleaning up..."
    echo "----------------------${NC}"
    rm -rf "$LOG_PATH" "$LIB_PATH" $PROGRAM_EXAMPLE_PATH
    echo "All clean!"
    exit 0
}

# SCRIPT
# ------

# Argument handling
if [ "$1" = "--clean" ]; then
    clean_up
elif [ $# -gt 0 ]; then
    echo "${ERROR}[ERROR] Invalid argument: $1"
    echo "${INFO}[USAGE] ./my_script.sh [--clean]${NC}"
    exit 1
fi

# Setup venv
echo "${INFO}[INFO] Setting up virtual env - venv..."
echo "---------------------------------------${NC}"
$PYTHON_PATH -m virtualenv $LIB_PATH
. $LIB_PATH/bin/activate
echo "Virtual env activated: $LIB_PATH"

# Upgrade pip and print its version
echo "\n${INFO}[INFO] Upgrading pip..."
echo "-----------------------${NC}"
$LIB_PATH/bin/python3 -m pip install --upgrade pip

echo "\n${INFO}[INFO] pip version:"
echo "-------------------${NC}"
$LIB_PATH/bin/python3 -m pip --version

# Pip install
echo "\n${INFO}[INFO] Installing path.py library:"
echo "----------------------------------${NC}"
$LIB_PATH/bin/python3 -m pip install --log $LOG_PATH --force-reinstall --upgrade git+$PATH_PY_URL
export PYTHONPATH=$LIB_PATH/lib/python3.*/site-packages

# Execute the small program
echo "\n${INFO}[INFO] Executing $PROGRAM_PATH:"
echo "-------------------------------${NC}"
$LIB_PATH/bin/python3 $PROGRAM_PATH

# Clean up and deactivate venv
echo "\n${INFO}[INFO] Deactivating virtual env..."
echo "----------------------------------${NC}"
deactivate
echo "Virtual env deactivated: $LIB_PATH"


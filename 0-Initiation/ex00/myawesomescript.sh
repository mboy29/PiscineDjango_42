#!/bin/sh

# Define ANSI color escape codes
ERROR='\033[0;31m'
SUCCESS='\033[0;32m'
INFO='\033[0;34m'
WARNING='\033[0;33m'
NC='\033[0m'

# Check if there are too many parameters
if [ $# -gt 1 ]; then
    echo "${ERROR}[ERROR] Too many parameters provided${NC}"
    echo "${WARNING}[USAGE] $0 <bit.ly link>${NC}"
    exit 1
fi

# Check if a bit.ly link is provided
if [ -z "$1" ]; then
    echo "${ERROR}[ERROR] No bit.ly link provided${NC}"
    echo "${WARNING}[USAGE] $0 <bit.ly link>${NC}"
    exit 1
fi

# Strip 'http://' or 'https://' from the provided link if present
link="$1"
link=${link#http://}
link=${link#https://}

# Check if the modified parameter starts with "bit.ly/"
if ! echo "$link" | grep -q "^bit\.ly\/.*$"; then
    echo "${ERROR}[ERROR] Not a valid bit.ly link${NC}"
    echo "${WARNING}[USAGE] $0 <bit.ly link>${NC}"
    exit 1
fi

# Retrieve the real address using curl and extract the URL :
# - curl -sI: Send a HEAD request and don't show the progress bar
# - grep -i 'location:': Search for the 'location:' header (case-insensitive)
# - cut -d' ' -f2: Split the line by spaces and get the second field
# - tr -d '\r': Remove the carriage return character
real_address=$(curl -sI "http://$link" | grep -i 'location:' | cut -d' ' -f2 | tr -d '\r')

# Output the real address
echo "${SUCCESS}$real_address${NC}"

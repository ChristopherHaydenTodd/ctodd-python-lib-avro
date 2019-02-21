#!/usr/bin/env bash
#
# Test Python Package Package
#
# Example Call:
#    ./test.sh
#

SETUP_FILE="./setup.py"

# Parse CLI Arguments
while [[ $# -gt 0 ]]
do
    key="$1"
    case $key in
        -S|-s|--setup)
        SETUP_FILE="$2"
        shift
        shift
        ;;
        --setup=*)
        SETUP_FILE="${1#*=}"
        shift
        ;;
        *)
        shift
        ;;
    esac
done

echo "$(date +%c): Running Unit Tests (Setup File = ${SETUP_FILE})"
python3 ${SETUP_FILE} test

TEST_STATUS=$?
echo "$(date +%c): Test Exit Status - ${TEST_STATUS}"

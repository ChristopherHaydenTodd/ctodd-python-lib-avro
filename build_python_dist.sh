#!/usr/bin/env bash
#
# Build Python Package For Pushing to Repository
#
# Example Call:
#    ./build.sh {--setup=./setup.py}
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
        -F|-f|--file|--filename)
        SETUP_FILE="$2"
        shift
        shift
        ;;
        --file=*|--filename=*)
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
if [ ${TEST_STATUS} != "0" ]
then
    echo "$(date +%c): Tests Failed, Not Building"
    exit 1
fi

echo "$(date +%c): Building Python Package (Setup File = ${SETUP_FILE})"
python3.6 ${SETUP_FILE} sdist bdist_wheel

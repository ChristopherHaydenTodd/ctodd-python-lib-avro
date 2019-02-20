#!/usr/bin/env bash
#
# Clean Previously Built Python Package Package
#
# Example Call:
#    ./clean.sh
#

echo "$(date +%c): Cleaning Built Package (Removing Previous Builds)"
rm -rf ./.coverage ./.eggs/ ./*.egg-info/ ./.pytest_cache/ ./__pycache__ ./build/ ./dist/ ./htmlcov/

#!/usr/bin/env bash
#
# Install Python Dependencies For The Script
#

echo "$(date +%c): Installing Python Packages For the Package"
pip3 install -r avro_helpers/requirements.txt

echo "$(date +%c): Installing Python Packages For Testing the Package"
pip3 install -r avro_helpers/tests/requirements.txt


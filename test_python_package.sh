#!/usr/bin/env bash
#
# Test Python Package Package
#
# Example Call:
#    ./test.sh
#

echo "$(date +%c): Testing Package"
pytest --color=yes --cov=avro_helpers --cov-fail-under=75 --cov-report=html --cov-report=term --maxfail=999 --verbose

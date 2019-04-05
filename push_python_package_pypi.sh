#!/usr/bin/env bash
#
# Push Package To Repository
#
# Example Call:
#    ./push.sh --repository=http://localhost:8081/repository/pypi/
#

PYPI="pypi"
USERNAME=""
PASSWORD=""
BUILD_DIR="./dist/*"

# Parse CLI Arguments
while [[ $# -gt 0 ]]
do
    key="$1"
    case $key in
        --pypi=*)
        PYPI="${1#*=}"
        shift
        ;;
        --username=*)
        USERNAME="${1#*=}"
        shift
        ;;
        --password=*)
        PASSWORD="${1#*=}"
        shift
        ;;
        *)
        shift
        ;;
    esac
done

echo "$(date +%c): PyPi = ${PYPI}"

if [ -z "$(ls -A ${BUILD_DIR})" ]; then
   echo "$(date +%c): Build Dir is Empty, Nothing to Push. Maybe need to Build First?"
   exit 1
fi

echo "$(date +%c): Pushing Pushing Package (${BUILD_DIR}) to ${REPOSITORY}"
if ([ -z "${USERNAME}" ] || [ -z "${PASSWORD}" ])
then
    echo "$(date +%c): No Username, Pushing without"
    twine upload --repository=${PYPI} ${BUILD_DIR}
else
    echo "$(date +%c): Pushing with Specified User: ${USERNAME}"
    twine upload --repository=${PYPI} --username=${USERNAME} --password=${PASSWORD} ${BUILD_DIR}
fi

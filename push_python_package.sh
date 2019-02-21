#!/usr/bin/env bash
#
# Push Package To Repository
#
# Example Call:
#    ./push.sh --repository=http://localhost:8081/repository/pypi/
#

REPOSITORY_PROTOCOL="https"
REPOSITORY_PORT="8081"
REPOSITORY_HOST=""
REPOSITORY_PYPI="pypi"
USERNAME=""
PASSWORD=""
BUILD_DIR="./dist/*"

# Parse CLI Arguments
while [[ $# -gt 0 ]]
do
    key="$1"
    case $key in
        --repo_protocol=*)
        REPOSITORY_PROTOCOL="${1#*=}"
        shift
        ;;
        --repo_port=*)
        REPOSITORY_PORT="${1#*=}"
        shift
        ;;
        --repo_host=*)
        REPOSITORY_HOST="${1#*=}"
        shift
        ;;
        --repo_pypi=*)
        REPOSITORY_PYPI="${1#*=}"
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

REPOSITORY="${REPOSITORY_PROTOCOL}://${REPOSITORY_HOST}:${REPOSITORY_PORT}/repository/${REPOSITORY_PYPI}/"
echo "$(date +%c): Repository = ${REPOSITORY}"

if [ -z "$(ls -A ${BUILD_DIR})" ]; then
   echo "$(date +%c): Build Dir is Empty, Nothing to Push. Maybe need to Build First?"
   exit 1
fi

echo "$(date +%c): Pushing Pushing Package (${BUILD_DIR}) to ${REPOSITORY}"
if ([ -z "${USERNAME}" ] || [ -z "${PASSWORD}" ])
then
  echo "$(date +%c): No Username, Pushing without"
  twine upload --repository-url=${REPOSITORY} ${BUILD_DIR}
else
  echo "$(date +%c): Pushing with Specified User: ${USERNAME}"
  twine upload --username=${USERNAME} --password=${PASSWORD} --repository-url=${REPOSITORY} ${BUILD_DIR}
fi

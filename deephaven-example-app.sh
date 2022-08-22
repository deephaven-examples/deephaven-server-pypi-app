#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
# set -o xtrace

__venv="${VIRTUAL_ENV:-$(mktemp -d)/venv}"
__pip="${__venv}/bin/pip"
__python="${__venv}/bin/python"
__java_home="${__venv}/bin/java-home"

if [[ ! -f "${__python}" ]]; then
    echo "Creating virtual environment @ '${__venv}'"
    python3 -m venv "${__venv}"
else
  echo "Using existing virtual environment '${__venv}'"
fi

echo "Installing requirements..."

"${__pip}" install -q --upgrade pip

"${__pip}" install -q \
    "jpy>=0.11.1.dev0" \
    java-utilities \
    deephaven-example-app

if [[ -z "${JAVA_HOME:-}" ]]; then
    JAVA_HOME="$("${__java_home}")"
    echo "Found '${JAVA_HOME}', presuming JAVA_HOME"
else
    echo "Using existing JAVA_HOME, '${JAVA_HOME}'"
fi

JAVA_HOME="${JAVA_HOME}" \
    "${__python}" -m deephaven_example_app


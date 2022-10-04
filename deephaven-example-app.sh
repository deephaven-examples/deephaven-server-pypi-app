#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
# set -o xtrace

__venv="${VIRTUAL_ENV:-$(mktemp -d)/venv}"
__pip="${__venv}/bin/pip"
__python="${__venv}/bin/python"

if [[ ! -f "${__python}" ]]; then
    echo "Creating virtual environment @ '${__venv}'"
    python3 -m venv "${__venv}"
else
  echo "Using existing virtual environment '${__venv}'"
fi

echo "Installing requirements..."

"${__pip}" install -q --upgrade setuptools pip

"${__pip}" install -q deephaven-example-app>=0.3.0

"${__python}" -m deephaven_example_app

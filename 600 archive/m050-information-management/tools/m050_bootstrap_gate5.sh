#!/bin/sh
set -eu

MEDIAN_REPO_ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
MEDIAN_ENGINE_DIR="$MEDIAN_REPO_ROOT/m050/extraction/engine"
MEDIAN_VENV_DIR="$MEDIAN_REPO_ROOT/.venv"
MEDIAN_BOOTSTRAP_PYTHON=${MEDIAN_BOOTSTRAP_PYTHON:-/opt/anaconda3/bin/python3.12}

if [ "$(uname -m)" != "arm64" ]; then
    echo "Gate 5 bootstrap requires arm64 macOS" >&2
    exit 1
fi

if [ ! -x "$MEDIAN_BOOTSTRAP_PYTHON" ]; then
    echo "Bootstrap interpreter not found: $MEDIAN_BOOTSTRAP_PYTHON" >&2
    exit 1
fi

if [ ! -x "$MEDIAN_VENV_DIR/bin/python" ]; then
    "$MEDIAN_BOOTSTRAP_PYTHON" -m venv "$MEDIAN_VENV_DIR"
fi

"$MEDIAN_VENV_DIR/bin/python" -m pip install \
    --require-hashes \
    -r "$MEDIAN_ENGINE_DIR/requirements.lock"
"$MEDIAN_VENV_DIR/bin/python" -m pip install \
    --no-build-isolation \
    --no-deps \
    -e "$MEDIAN_ENGINE_DIR"
"$MEDIAN_VENV_DIR/bin/median-gate5" preflight \
    --lock "$MEDIAN_ENGINE_DIR/requirements.lock"
"$MEDIAN_VENV_DIR/bin/python" -m pytest "$MEDIAN_ENGINE_DIR/tests"
"$MEDIAN_VENV_DIR/bin/python" "$MEDIAN_REPO_ROOT/m050/tools/m050_guard.py" --with-tests

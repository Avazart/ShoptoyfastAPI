#!/bin/bash


if uname -s | grep -qE 'NT|CYGWIN|MINGW'; then
    WINDOWS=True
    PYTHON=python
else
    WINDOWS=False
    PYTHON=python3
fi


if [[ ! -d ".venv" ]]; then
   $PYTHON -m venv .venv
fi


if [[ "$WINDOWS" == "True" ]]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi

if [[ $? -eq 0 && "$VIRTUAL_ENV" ]]; then
    echo -e "Virtual environment activated.\n$VIRTUAL_ENV"
    python -V
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    echo "Done!"
else
    echo "Error: Failed to activate the virtual environment." >&2
fi
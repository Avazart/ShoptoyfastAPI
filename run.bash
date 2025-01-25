#!/bin/bash
if uname -s | grep -qE 'NT|CYGWIN|MINGW'; then
    WINDOWS=True
    PYTHON=python
else
    WINDOWS=False
    PYTHON=python3
fi

if [[ "$WINDOWS" == "True" ]]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi
$PYTHON -m uvicorn src.__main__:app --reload
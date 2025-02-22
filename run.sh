#!/bin/bash

if [ -d ".venv" ]; then
    echo ".venv already exists"
else
    echo "Virtual environment doesn't exist"
    exit 1
fi

source .venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Failed to activate virtual environment"
    exit 1
fi

python3 client.py
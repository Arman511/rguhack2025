#!/bin/bash

if [ -d ".venv" ]; then
    echo ".venv already exists"
else
    python3 -m venv .venv
    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment"
        exit 1
    fi
fi

source .venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Failed to activate virtual environment"
    exit 1
fi

pip install --upgrade pip
if [ $? -ne 0 ]; then
    echo "Failed to upgrade pip"
    exit 1
fi

pip install -r requirements.txt -U
if [ $? -ne 0 ]; then
    echo "Failed to install requirements"
    exit 1
fi
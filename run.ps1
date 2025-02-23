if (Test-Path ".venv") {
    Write-Output ".venv already exists"
} else {
    Write-Output "Virtual environment doesn't exist"
    exit 1
}

try {
    .venv\Scripts\Activate.ps1
} catch {
    Write-Output "Failed to activate virtual environment"
    exit 1
}

python client.py


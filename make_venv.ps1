if (Test-Path ".venv") {
    Write-Output ".venv already exists"
} else {
    python3 -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        Write-Output "Failed to create virtual environment"
        exit 1
    }
}

.\.venv\Scripts\Activate.ps1
if ($LASTEXITCODE -ne 0) {
    Write-Output "Failed to activate virtual environment"
    exit 1
}

pip install --upgrade pip
if ($LASTEXITCODE -ne 0) {
    Write-Output "Failed to upgrade pip"
    exit 1
}

pip install -r requirements.txt -U
if ($LASTEXITCODE -ne 0) {
    Write-Output "Failed to install requirements"
    exit 1
}
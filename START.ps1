# Micro Banking System - PowerShell Quick Start Script
# Run: .\START.ps1

Write-Host "`n" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   MICRO BANKING SYSTEM - QUICK START" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Check if Python is installed
try {
    python --version | Out-Null
}
catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.10 or higher" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Create virtual environment if it doesn't exist
if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
    Write-Host ""
}

# Activate virtual environment
& ".\.venv\Scripts\Activate.ps1"

# Check if dependencies are installed
$packages = pip list | Select-String "fastapi"
if (-not $packages) {
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    pip install -r requirements.txt
    Write-Host ""
}

# Start server in background
Write-Host "Starting API Server on http://127.0.0.1:8000..." -ForegroundColor Green
Start-Process -NoNewWindow -FilePath ".\.venv\Scripts\python.exe" `
    -ArgumentList "-m uvicorn api_server:app --reload --port 8000"

Write-Host "Waiting for server to start..." -ForegroundColor Yellow
Start-Sleep -Seconds 3

# Start client
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "   Starting Banking Client..." -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

& ".\.venv\Scripts\python.exe" api_client.py

# Keep window open if there's an error
Read-Host "`nPress Enter to exit"

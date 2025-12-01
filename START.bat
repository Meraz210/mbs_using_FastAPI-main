@echo off
REM Micro Banking System - Quick Start Script
REM Run this batch file to start the system automatically

echo.
echo ========================================
echo   MICRO BANKING SYSTEM - QUICK START
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.10 or higher
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
    echo.
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Check if requirements are installed
pip show fastapi >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    echo.
)

REM Start server in background and client
echo Starting API Server on http://127.0.0.1:8000...
start "Banking Server" .venv\Scripts\python.exe -m uvicorn api_server:app --reload --port 8000

echo Waiting for server to start...
timeout /t 3 /nobreak

echo.
echo ========================================
echo   Starting Banking Client...
echo ========================================
echo.

.venv\Scripts\python.exe api_client.py

pause

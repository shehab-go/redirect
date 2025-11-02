@echo off
chcp 65001 >nul
title Droidify Redirector Server
color 0A

echo.
echo ============================================================
echo    🚀 Droidify Redirector - Starting Server...
echo ============================================================
echo.

python server.py

if errorlevel 1 (
    echo.
    echo ❌ Error: Python not found or server failed to start!
    echo 💡 Make sure Python is installed and in PATH
    echo.
    pause
)


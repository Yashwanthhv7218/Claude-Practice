@echo off
REM Resume Markdown to HTML Auto-Sync Script
REM Run this script anytime you edit resume.md to regenerate resume.html

echo.
echo ================================
echo  Resume Auto-Sync Tool
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.6+ or add it to your system PATH
    pause
    exit /b 1
)

REM Check if resume.md exists
if not exist "resume.md" (
    echo Error: resume.md not found in current directory
    echo Please run this script from the folder containing resume.md
    pause
    exit /b 1
)

REM Run the sync script
echo Running sync... (resume.md to resume.html)
echo.
python sync_resume.py

if %errorlevel% equ 0 (
    echo.
    echo ✓ Success! resume.html has been updated
    echo.
    echo Next steps:
    echo   1. Open resume.html in your browser to verify
    echo   2. Commit both files to git
    echo   3. Push to GitHub Pages
    echo.
) else (
    echo.
    echo ✗ Sync failed. Please check the error above.
    echo.
)

pause

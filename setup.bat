@echo off
echo Checking if Python is installed...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed or not added to PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo and make sure to select "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo Checking if pip is installed and up-to-date...
python -m pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] pip is not installed or not working correctly.
    echo Attempting to install pip...
    python -m ensurepip --default-pip >nul 2>&1
    IF %ERRORLEVEL% NEQ 0 (
        echo [ERROR] Failed to install pip. Please reinstall Python and ensure pip is included.
        pause
        exit /b 1
    )
    echo pip installed successfully.
) ELSE (
    echo Updating pip...
    python -m pip install --upgrade pip >nul 2>&1
    IF %ERRORLEVEL% NEQ 0 (
        echo [ERROR] Failed to update pip. Please check your internet connection.
        pause
        exit /b 1
    )
    echo pip is up to date.
)

echo Installing required packages...
python -m pip install pystyle >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to install the required package: pystyle.
    echo Please check your internet connection or try running:
    echo python -m pip install pystyle
    pause
    exit /b 1
)

echo All checks passed and packages installed successfully.
pause
exit

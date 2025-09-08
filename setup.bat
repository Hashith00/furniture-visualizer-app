@echo off
echo Setting up Furniture Visualizer App...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo Installing required packages...
pip install -r requirements.txt

echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. Get your Gemini API key from https://aistudio.google.com/apikey
echo 2. Edit the .env file and replace 'your_actual_api_key_here' with your API key
echo 3. Run: streamlit run app.py
echo.
pause

@echo off
echo 🏠 Furniture Visualizer App
echo ========================
echo.

REM Check if .env file has API key
findstr /C:"your_actual_api_key_here" .env >nul
if %errorlevel% equ 0 (
    echo ⚠️  WARNING: Please set your actual API key in the .env file
    echo Edit .env and replace 'your_actual_api_key_here' with your Gemini API key
    echo Get your key from: https://aistudio.google.com/apikey
    echo.
    pause
    exit /b 1
)

echo ✅ API key configured
echo 🚀 Starting Streamlit app...
echo.
echo The app will open in your browser at http://localhost:8501
echo Press Ctrl+C to stop the app
echo.

streamlit run app.py

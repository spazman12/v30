@echo off
echo Installing Steam Tools Generator dependencies...
echo.

echo Installing core dependencies...
pip install requests Pillow

echo.
echo Steam Tools Generator is ready to use!
echo.
echo To run the application:
echo   cd v30
echo   python steam_tools_generator.py
echo.
echo Note: Steam authentication features require additional packages.
echo To enable them, uncomment the Steam dependencies in requirements.txt
echo and run: pip install -r requirements.txt
echo.
pause

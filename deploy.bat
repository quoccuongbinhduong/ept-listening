@echo off
echo ===================================
echo   EPT LISTENING AUTO DEPLOYMENT
echo ===================================
echo.
echo 1. Preparing files...
python prepare_deploy.py
if %errorlevel% neq 0 (
    echo [ERROR] Failed to prepare files!
    pause
    exit /b %errorlevel%
)

echo.
echo 2. Committing and pushing to GitHub...
cd /d D:\EPT\ept-deploy
git add .
git commit -m "Auto deploy website update"
git push origin HEAD:main

echo.
echo ===================================
echo   DEPLOYMENT COMPLETE!
echo ===================================
pause

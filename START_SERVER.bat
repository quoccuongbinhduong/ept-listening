@echo off
title EPT Listening Practice Server
echo.
echo  ================================================
echo   EPT Listening Practice - TDMU
echo  ================================================
echo.

:: Chuyen den thu muc chua file
cd /d "D:\EPT\Listening"

:: Kiem tra index.html ton tai khong
if not exist "index.html" (
    echo  [LOI] Khong tim thay index.html trong D:\EPT\Listening\
    echo  Hay chac chan ban dang chay file nay tu dung vi tri.
    pause
    exit /b 1
)

:: Kiem tra Python
python --version >nul 2>&1
if errorlevel 1 (
    echo  [LOI] Khong tim thay Python!
    echo  Hay cai Python tu python.org
    pause
    exit /b 1
)

:: Lay IP local (lay dong dau tien co IPv4)
set IP=127.0.0.1
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /i "IPv4"') do (
    set RAWIP=%%a
    goto :foundip
)
:foundip
:: Xoa khoang trang
set IP=%RAWIP: =%

echo  Dang khoi dong server...
echo.
echo  ================================================
echo  Server dang chay tai:
echo.
echo    Tren may tinh nay  : http://localhost:8088
echo    Tren dien thoai    : http://%IP%:8088
echo.
echo  De su dung tren Android:
echo    1. Ket noi cung mang WiFi voi may tinh
echo    2. Mo Chrome tren dien thoai
echo    3. Nhap dia chi: http://%IP%:8088
echo    4. Hoac truy cap: http://%IP%:8088/index.html
echo.
echo  Nhan Ctrl+C de dung server.
echo  ================================================
echo.

:: Mo browser voi duong dan day du
start "" "http://localhost:8088/index.html"

:: Chay server TU THU MUC HIEN TAI (D:\EPT\Listening)
python server.py

pause

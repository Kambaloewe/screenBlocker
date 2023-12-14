@echo off
title Bulder for BuildYourOwnBusiness
color 8
echo "//////////////////////////////////////"
echo "// ____        _ _     _            //"
echo "//| __ ) _   _| (_) __| | ___ _ __  //"
echo "//|  _ \| | | | | |/ _` |/ _ | '__| //"
echo "//| |_) | |_| | | | (_| |  __| |    //"
echo "//|____/ \__,_|_|_|\__,_|\___|_|    //"
echo "//////////////////////////////////////"

timeout /t 1

pip install pyinstaller
pip install tk
pip install thinker

echo #
echo # Installation completed, create EXE FILE
echo #

curl.exe https://github.com/Kambaloewe/screenBlocker/blob/main/BuildYourOwnBusiness -o BuildYourOwnBusiness.py
timeout /t 3

REM Kompiliere die Python-Datei mit PyInstaller
C:\Users\%USERNAME%\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller --noconfirm --onefile --windowed "C:\Users\%USERNAME%\Downloads\BuildYourOwnBusiness.py"

echo #
echo # Requirements installed, Safed EXE FILE: /dist/BulidYourOwnBussines.exe
echo #
pause

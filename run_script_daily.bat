@echo off

setlocal ENABLEDELAYEDEXPANSION

set "mo=%Date:~4,2%"
if "%mo:~0,1%"=="0" set "mo=%mo:~1%"
set names=JanFebMarAprMayJunJulAugSepOctNovDec
set /a "pos = 3 * %mo%" - 3
set "ti=!names:~%pos%,3!"

set "date=%ti% %Date:~7,2%, %Date:~10,4%"

cd /d C:\SWE Projects\rekhta-words\venv\Scripts && activate && cd /d C:\SWE Projects\rekhta-words && python script.py && git add . && git commit -m "Words till %date%" && git push origin master
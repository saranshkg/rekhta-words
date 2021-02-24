@echo off

for /f "delims=" %%a in ('wmic OS Get localdatetime ^| find "."') do set dt=%%a
set year=%dt:~0,4%
set month=%dt:~4,2%
set day=%dt:~6,2%

if %month%==01 set monthname=Jan
if %month%==02 set monthname=Feb
if %month%==03 set monthname=Mar
if %month%==04 set monthname=Apr
if %month%==05 set monthname=May
if %month%==06 set monthname=Jun
if %month%==07 set monthname=Jul
if %month%==08 set monthname=Aug
if %month%==09 set monthname=Sep
if %month%==10 set monthname=Oct
if %month%==11 set monthname=Nov
if %month%==12 set monthname=Dec


set "date_formatted=%monthname% %day%, %year%"

cd /d C:\SWE Projects\rekhta-words\venv\Scripts && activate && cd /d C:\SWE Projects\rekhta-words && python script.py && git add . && git commit -m "Words last updated on %date_formatted%" && git push origin master


@echo off

echo "current settings are:"
echo path = %path%

set id=%username%
set /p id="Enter user name(default %username%): "
set password=""
set /p password="Enter password: " 

python -V >nul 
if errorlevel 1 (
  goto pythonNotFound
)
goto eod1

:pythonNotFound
echo Error^: Python not configured in environment variables
set pythonhome=C:\Program Files\Python36
set /p pythonhome="Enter python home(default %pythonhome%): "
set path=%path%%pythonhome%;%pythonhome%\Scripts


:eod1

psql -V >nul 
if errorlevel 1 (
 goto psqlNotFound
)
goto eod2

:psqlNotFound
echo Error^: postgres not configured in environment variables
set postgrehome=C:\Program Files (x86)\PostgreSQL\9.3\bin
set /p postgrehome="Enter postgres home(default %postgrehome%): "
set path=%path%%postgrehome%


:eod2

echo %http_proxy%


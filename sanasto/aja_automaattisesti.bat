@echo off
:uusinta
echo ---
echo Käynnistetään suodatus...
python suodata_yleiskieli.py --jatka
IF %ERRORLEVEL% NEQ 0 (
    echo ---
    echo Ohjelma keskeytyi, odotetaan 2 sekuntia ja yritetään uudestaan...
    timeout /t 1 >nul
    goto uusinta
)
echo ---
echo Ohjelma päättyi onnistuneesti.
pause

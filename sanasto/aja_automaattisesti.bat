@echo off
:uusinta
echo ---
echo Käynnistetään suodatus...
python suodata_yleiskieli.py --jatka
IF %ERRORLEVEL% NEQ 0 (
    echo ---
    echo Ohjelma keskeytyi, odotetaan 10 sekuntia ja yritetään uudestaan...
    timeout /t 10 >nul
    goto uusinta
)
echo ---
echo Ohjelma päättyi onnistuneesti.
pause

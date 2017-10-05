@echo off
title LemonBot
mode con:cols=70 lines=7

:launch
echo Lanzando LemonBot...
echo.
python bot.py

echo.
echo Sesion Terminada
echo.
echo --------------------
echo.
goto launch

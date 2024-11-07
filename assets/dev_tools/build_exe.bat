@echo off

cd /d %~dp0

cd ../..

hatch run build:exe

exit /b 0
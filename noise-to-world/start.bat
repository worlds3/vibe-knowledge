@echo off
cd /d "%~dp0"
start "" http://localhost:8737
python -m http.server 8737

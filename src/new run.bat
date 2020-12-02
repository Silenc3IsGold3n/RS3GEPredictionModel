@echo off
python updateSpreadsheet.py
if %ERRORLEVEL% == 1 (
	EXIT /B %ERRORLEVEL%
)

@echo off

cd /d %~dp0

set "py_project_dev_tools_exe=%CD%\py_project_dev_tools.exe"

set "toml=%CD%\..\..\pyproject.toml"

"%py_project_dev_tools_exe%" lint_code "%toml%"

exit /b 0



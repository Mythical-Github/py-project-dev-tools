@echo off

cd /d %~dp0

set "exe_suffix=dist/py_project_dev_tools.exe"
set "py_project_dev_tools_exe=%CD%/%exe_suffix%"

%py_project_dev_tools_exe% setup_virtual_environment "C:\Users\Mythical\Documents\GitHub\New folder\UnrealAutoMod\pyproject.toml"

exit /b 0
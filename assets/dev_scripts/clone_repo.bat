@echo off

cd /d %~dp0

cd ../..

set "repo_url=https://github.com/Mythical-Github/UnrealAutoMod"
set "repo_branch=main"
set "clone_recursively=False"
set "output_directory=C:/Users/Mythical/Documents/GitHub/New folder"

set "exe_suffix=dist/py_project_dev_tools.exe"
set "py_project_dev_tools_exe=%CD%/%exe_suffix%"

%py_project_dev_tools_exe% clone_repo "%repo_url%" %repo_branch% %clone_recursively% "%output_directory%"

exit /b 0
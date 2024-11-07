@echo off

cd /d %~dp0

set "dev_tools_dir=%CD%"

cd ../..

set "dir_to_zip=%dev_tools_dir%"
set "output_zip=%CD%/dist/dev_tools.zip"

set "exe_suffix=dist/py_project_dev_tools.exe"
set "py_project_dev_tools_exe=%CD%/%exe_suffix%"

"%py_project_dev_tools_exe%" zip_directory "%dir_to_zip%" "%output_zip%"

exit /b 0
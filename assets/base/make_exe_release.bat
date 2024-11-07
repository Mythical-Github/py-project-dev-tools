@echo off

cd /d %~dp0

cd ../..

set "toml_path=%CD%/pyproject.toml"
set "dir_to_zip=%CD%/assets/base"
set "output_zip_dir=%CD%/dist"

set "exe_suffix=dist/py_project_dev_tools.exe"
set "py_project_dev_tools_exe=%CD%/%exe_suffix%"

"%py_project_dev_tools_exe%" make_exe_release "%toml_path%" "%dir_to_zip%" "%dir_to_zip%" "%output_zip_dir%"

exit /b 0

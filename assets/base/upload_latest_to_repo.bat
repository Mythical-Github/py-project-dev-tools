@echo off

cd /d %~dp0

cd ../..

set "exe_suffix=dist/py_project_dev_tools.exe"
set "py_project_dev_tools_exe=%CD%/%exe_suffix%"

set "repo_branch=main"

set "toml=%CD%/pyproject.toml"

"%py_project_dev_tools_exe%" upload_latest_to_repo "%toml%" %repo_branch%

exit /b 0
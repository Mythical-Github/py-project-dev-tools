import os
import sys
import shutil
import tomllib
import subprocess
from pathlib import Path

import requests

from py_project_dev_tools import log_py as log


if getattr(sys, 'frozen', False):
    SCRIPT_DIR = Path(sys.executable).parent
else:
    SCRIPT_DIR = Path(__file__).resolve().parent


# hatch run scripts:refresh-deps: create a new requirements.txt with fresh dependencies
# hatch run build:exe: Create a UnreaAutoMod.exe in the dist folder
# hatch run scripts:clean: remove all untracked, and gitignored files
# hatch shell: Enter a virtual environment which has all dependencies automatically installed


def run_command(command, shell=False, input_working_dir=os.getcwd()):
    result = subprocess.run(command, shell=shell, text=True, cwd=input_working_dir)
    if result.returncode != 0:
        log.log_message(f'Command failed: {' '.join(command) if isinstance(command, list) else command}')
        sys.exit(result.returncode)


def load_toml_data(input_toml_path: str):
    with open(input_toml_path, 'rb') as f:
        return tomllib.load(f)


def clone_repo(input_url: str, input_branch_name: str, clone_recursively: bool, output_directory: str):
    log.log_message(f'Cloning repository from {input_url}, branch {input_branch_name}...')
    if clone_recursively:
        run_command(['git', 'clone', '--recurse-submodules', '-b', input_branch_name, input_url], input_working_dir=output_directory)
    else:
        run_command(['git', 'clone', '-b', input_branch_name, input_url], input_working_dir=output_directory)


def refresh_deps(input_toml_path: str):
    log.log_message('Refreshing dependencies...')
    toml_dir = os.path.dirname(input_toml_path)
    run_command(['hatch', 'run', "scripts:refresh-deps"], input_working_dir=toml_dir)


        # "install_hatch": {
        #     "function_name": "install_hatch",
        #     "arg_help_pairs": [
        #         {"project_toml_path": "Path to the pyproject.toml"}
        #     ]
        # },
        # "install_git": {
        #     "function_name": "install_git",
        #     "arg_help_pairs": [
        #         {"project_toml_path": "Path to the pyproject.toml"}
        #     ]
        # },


# def is_hatch_installed(input_toml_path: str) -> bool:
#     if os.path.exists(get_hatch_install_path(input_toml_path)):
#         return True
#     else:
#         return False


# def get_hatch_install_path(input_toml_path: str) -> str:
#     toml_dir = os.path.dirname(input_toml_path)
#     return f'{toml_dir}/assets/programs/hatch-universal.exe'


# def get_hatch_path(input_toml_path: str) -> str:
#     if not is_hatch_installed(input_toml_path):
#         install_hatch(input_toml_path)
#     return get_hatch_install_path(input_toml_path)


# def install_hatch(input_toml_path: str):
#     url = 'https://github.com/pypa/hatch/releases/latest/download/hatch-universal.exe'
#     log.log_message('Downloading hatch-universal.exe...')
#     response = requests.get(url, stream=True)
#     response.raise_for_status()
#     hatch_dir = os.path.dirname(get_hatch_install_path(input_toml_path))
#     if not os.path.isdir(hatch_dir):
#         os.makedirs(hatch_dir)
#     with open(get_hatch_install_path(input_toml_path), 'wb') as file:
#         for chunk in response.iter_content(chunk_size=8192):
#             file.write(chunk)
#     log.log_message(f'Download completed and saved to {get_hatch_install_path(input_toml_path)}')


# def install_git(input_toml_path: str):
#     pass


def test_virtual_environment(input_toml_path: str):
    pass


def cleanup_repo(input_toml_path: str):
    pass


def upload_latest_to_repo(input_url: str, branch_name: str):
    pass


def setup_virtual_environment(input_toml_path: str):
    log.log_message('Setting up virtual environment...')
    toml_dir = os.path.dirname(input_toml_path)
    run_command(['hatch', 'shell', '--name', 'shell_name_test'], input_working_dir=toml_dir)


def make_all_release(input_toml_path: str):
    pass
def make_exe_release(input_toml_path: str):
    pass
def test_exe_release(input_toml_path: str):
    pass
def make_dev_tools_release(input_toml_path: str):
    pass
import sys
import tomllib
import requests
import subprocess
from pathlib import Path


# hatch run scripts:refresh-deps: create a new requirements.txt with fresh dependencies
# hatch run build:exe: Create a UnreaAutoMod.exe in the dist folder
# hatch run scripts:clean: remove all untracked, and gitignored files
# hatch shell: Enter a virtual environment which has all dependencies automatically installed


def run_command(command, shell=False):
    result = subprocess.run(command, shell=shell, text=True)
    if result.returncode != 0:
        print(f"Command failed: {' '.join(command) if isinstance(command, list) else command}")
        sys.exit(result.returncode)


def load_toml_data(input_toml_path: str):
    with open(input_toml_path, "rb") as f:
        return tomllib.load(f)


def clone_repo(input_url: str, branch_name: str):
    pass


def make_dev_tools_release(input_toml_path: str):
    pass


def refresh_deps(input_toml_path: str):
    pass


def install_hatch(input_toml_path: str):
    pass


def install_git(input_toml_path: str):
    pass


def test_virtual_environment(input_toml_path: str):
    pass


def cleanup_repo(input_toml_path: str):
    pass


def test_exe_release(input_toml_path: str):
    pass


def make_exe_release(input_toml_path: str):
    pass


def upload_latest_to_repo(input_url: str, branch_name: str):
    pass


def setup_virtual_environment(input_toml_path: str):
    pass


def make_all_release(input_toml_path: str):
    pass

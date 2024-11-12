import os
import sys
import shutil
import tomllib
import zipfile
import subprocess
from pathlib import Path

from py_project_dev_tools import log_py as log


if getattr(sys, 'frozen', False):
    SCRIPT_DIR = Path(sys.executable).parent
else:
    SCRIPT_DIR = Path(__file__).resolve().parent


def run_app(exe_path: str, args: list = [], working_dir: str = None):
    command = [exe_path] + args
    log.log_message(f'Command: {" ".join(command)} is executing')
    if working_dir:
        if os.path.isdir(working_dir):
            os.chdir(working_dir)

    process = subprocess.Popen(command, cwd=working_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=False)
    
    for line in iter(process.stdout.readline, ''):
        log.log_message(line.strip())

    process.stdout.close()
    process.wait()
    log.log_message(f'Command: {" ".join(command)} finished')


def get_toml_dir(input_toml_path: str):
    return os.path.dirname(input_toml_path)


def load_toml_data(input_toml_path: str):
    with open(input_toml_path, 'rb') as f:
        return tomllib.load(f)


def clone_repo(input_url: str, input_branch_name: str, clone_recursively: bool, output_directory: str):
    log.log_message(f'Cloning repository from {input_url}, branch {input_branch_name}...')
    if not os.path.isdir(output_directory):
        os.makedirs(output_directory)
    
    exe = 'git'
    args = [
        'clone',
        '-b',
        input_branch_name,
        input_url
    ]

    if clone_recursively:
        args.insert(1, '--recurse-submodules')

    run_app(exe, args, working_dir=output_directory)


def refresh_deps(input_toml_path: str):
    log.log_message('Refreshing dependencies...')
    exe = 'hatch'
    args = [
        'run',
        'scripts:refresh-deps'
    ]
    run_app(exe_path=exe, args=args, working_dir=get_toml_dir(input_toml_path))


def test_virtual_environment(input_toml_path: str):
    module_name = load_toml_data(input_toml_path)['project']['name']
    log.log_message('Testing virtual environment...')
    exe = 'hatch'
    args = [
        'run',
        'python',
        '-m',
        module_name,
        '-h'
    ]
    run_app(exe_path=exe, args=args, working_dir=get_toml_dir(input_toml_path))


def cleanup_repo(input_toml_path: str):
    log.log_message('Cleaning up repo...')
    exe = 'hatch'
    args = [
        'run',
        'scripts:clean'
    ]
    run_app(exe_path=exe, args=args, working_dir=get_toml_dir(input_toml_path))
    

def setup_virtual_environment(input_toml_path: str):
    log.log_message('Setting up virtual environment...')
    exe = 'hatch'
    args = [
        'env',
        'create',
        'default'
    ]
    run_app(exe_path=exe, args=args, working_dir=get_toml_dir(input_toml_path))


def build_exe(input_toml_path: str):
    log.log_message('Building exe...')
    exe = 'hatch'
    args = [
        'run',
        'build:exe'
    ]
    run_app(exe_path=exe, args=args, working_dir=get_toml_dir(input_toml_path))


def zip_directory(dir_to_zip: str, output_zip_file: str):
    with zipfile.ZipFile(output_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dir_to_zip):
            for file in files:
                full_path = os.path.join(root, file)
                arc_name = os.path.relpath(full_path, start=dir_to_zip)
                zipf.write(full_path, arcname=arc_name)
    log.log_message(f'Directory "{dir_to_zip}" has been zipped to "{output_zip_file}"')


def make_exe_release(input_toml_path: str):
    log.log_message('Making exe release...')
    toml_dir = get_toml_dir(input_toml_path)
    dist_dir = f'{toml_dir}/dist'
    exe_name = load_toml_data(input_toml_path)['project']['name']
    dist_exe = f'{dist_dir}/{exe_name}.exe'
    build_exe(input_toml_path)
    output_exe_dir = f'{toml_dir}/assets/base'
    os.makedirs(output_exe_dir, exist_ok=True)
    final_exe_location = f'{output_exe_dir}/{exe_name}.exe'
    if os.path.isfile(final_exe_location):
        os.remove(final_exe_location)
    shutil.copy(dist_exe, final_exe_location)
    output_zip = f'{dist_dir}/{exe_name}.zip'
    zip_directory(output_exe_dir, output_zip)


def upload_latest_to_repo(input_toml_path: str, branch: str = 'main'):
    desc = input("Enter commit description: ")

    status_result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=get_toml_dir(input_toml_path))
    if status_result.returncode != 0 or not status_result.stdout.strip():
        log.log_message("No changes detected or not in a Git repository.")
        sys.exit(1)

    checkout_result = subprocess.run(["git", "checkout", branch], capture_output=True, text=True, cwd=get_toml_dir(input_toml_path))
    if checkout_result.returncode != 0:
        log.log_message(f"Failed to switch to the {branch} branch.")
        sys.exit(1)

    subprocess.run(["git", "add", "."], check=True, cwd=get_toml_dir(input_toml_path))

    commit_result = subprocess.run(["git", "commit", "-m", desc], capture_output=True, text=True, cwd=get_toml_dir(input_toml_path))
    if commit_result.returncode != 0:
        log.log_message("Commit failed.")
        sys.exit(1)

    push_result = subprocess.run(["git", "push", "origin", branch], capture_output=True, text=True, cwd=get_toml_dir(input_toml_path))
    if push_result.returncode != 0:
        log.log_message("Push failed.")
        sys.exit(1)

    log.log_message("Changes committed and pushed successfully.")


def make_dev_tools_release(input_toml_path: str):
    log.log_message('Making dev tools release...')
    toml_dir = get_toml_dir(input_toml_path)
    exe_name = load_toml_data(input_toml_path)['project']['name']
    output_exe_dir = os.path.join(toml_dir, 'assets', 'dev_tools')
    dist_dir = os.path.join(toml_dir, 'dist')
    os.makedirs(dist_dir, exist_ok=True)
    output_zip = f'{dist_dir}/{exe_name}_dev_tools.zip'
    zip_directory(output_exe_dir, output_zip)


def test_exe_release(input_toml_path: str):
    module_name = load_toml_data(input_toml_path)['project']['name']
    log.log_message('Testing exe release...')
    exe = f'{get_toml_dir(input_toml_path)}/assets/base/{module_name}.exe'
    args = [
        '-h'
    ]
    run_app(exe_path=exe, args=args, working_dir=get_toml_dir(input_toml_path))    


def unzip_zip(input_zip_path: str, output_files_dir: str):
    if not os.path.isdir(output_files_dir):
        os.makedirs(output_files_dir)
    
    with zipfile.ZipFile(input_zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_files_dir)
        
    log.log_message(f"Files from '{input_zip_path}' have been extracted to '{output_files_dir}'")

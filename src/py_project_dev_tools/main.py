import os
import platform
import shutil
import subprocess
import sys
import tomllib
import zipfile
from pathlib import Path

from py_project_dev_tools import log_py as log


if getattr(sys, 'frozen', False):
    SCRIPT_DIR = Path(sys.executable).parent
else:
    SCRIPT_DIR = Path(__file__).resolve().parent


def get_toml_dir(input_toml_path: str):
    return os.path.dirname(input_toml_path)


def load_toml_data(input_toml_path: str):
    with open(input_toml_path, 'rb') as f:
        return tomllib.load(f)
    

class UnsupportedOSError(Exception):
    pass


def get_os_arch_zip_suffix() -> str:
    os_name = platform.system().lower()
    arch = platform.machine().lower()

    if os_name == "windows":
        if arch in {"amd64", "x86_64"}:
            return "x86_64-pc-windows-msvc"
        elif arch in {"i386", "i686"}:
            return "i686-pc-windows-msvc"

    elif os_name == "linux":
        if arch == "aarch64":
            return "aarch64-unknown-linux-gnu"
        elif arch == "x86_64":
            return "x86_64-unknown-linux-gnu"

    raise UnsupportedOSError(f"Unsupported OS or architecture: {os_name} - {arch}")


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


def zip_directory(dir_to_zip: str, output_zip_file: str):
    with zipfile.ZipFile(output_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dir_to_zip):
            for file in files:
                full_path = os.path.join(root, file)
                arc_name = os.path.relpath(full_path, start=dir_to_zip)
                zipf.write(full_path, arcname=arc_name)
    log.log_message(f'Directory "{dir_to_zip}" has been zipped to "{output_zip_file}"')


def build_exes(input_toml_path: str):
    log.log_message('Building exes...')
    exe_name = load_toml_data(input_toml_path)['project']['name'].replace("-", "_")
    py_path = f'src/{exe_name}/__main__.py'
    pyw_path = f'{py_path}w'
    exe = 'uv'
    args = [
        'run',
        'pyinstaller',
        '--noconfirm',
        '--onefile',
        "--hidden-import=textual.widgets._tab",
        '--console', 
        '--name',
        f'{exe_name}',
        '--icon=assets/images/project_main_icon.ico',
        py_path
    ]
    run_app(exe_path=exe, args=args, working_dir=get_toml_dir(input_toml_path))

    log.log_message(f'Finished building exe from "{py_path}"...')

    if os.path.isfile(os.path.normpath(f'{os.path.dirname(input_toml_path)}/{pyw_path}')):
        args = [
            'run',
            'pyinstaller',
            '--noconfirm',
            '--onefile',
            "--hidden-import=textual.widgets._tab", 
            '--console', 
            '--name',
            f'{exe_name}_headless',
            '--icon=assets/images/project_main_icon.ico',
            pyw_path
        ]
        run_app(exe_path=exe, args=args, working_dir=get_toml_dir(input_toml_path))

        log.log_message(f'Finished building exe from "{pyw_path}"...')


def make_exe_release(input_toml_path: str):
    log.log_message('Making exe release...')
    main_exe_name = load_toml_data(input_toml_path)['project']['name'].replace("-", "_")

    exe_names = [main_exe_name, f'{main_exe_name}_headless']

    toml_dir = get_toml_dir(input_toml_path)
    dist_dir = f'{toml_dir}/dist'
    output_exe_dir = f'{toml_dir}/assets/base'
    os.makedirs(output_exe_dir, exist_ok=True)

    for exe_name in exe_names:
        if platform.system() == 'Windows':
            dist_exe = f'{dist_dir}/{exe_name}.exe'
            final_exe_location = f'{output_exe_dir}/{exe_name}.exe'
        else:
            dist_exe = f'{dist_dir}/{exe_name}'
            final_exe_location = f'{output_exe_dir}/{exe_name}'

        build_exes(input_toml_path)

        if os.path.isfile(final_exe_location):
            os.remove(final_exe_location)

        shutil.copy(dist_exe, final_exe_location)

    output_zip = f'{dist_dir}/{main_exe_name}.zip'
    zip_directory(output_exe_dir, output_zip)

    log.log_message(f'Executable release created at {output_zip}')


def make_exe_release_ci_cd(os_arch_line: str = get_os_arch_zip_suffix()):
    log.log_message('Making exe release...')

    input_toml_path = os.path.normpath(f"{os.getcwd()}/pyproject.toml")
    log.log_message(f"Reading TOML file: {input_toml_path}")
    main_exe_name = load_toml_data(input_toml_path)['project']['name'].replace("-", "_")

    exe_names = [main_exe_name, f'{main_exe_name}_headless']

    toml_dir = os.path.normpath(get_toml_dir(input_toml_path))
    dist_dir = os.path.normpath(f'{toml_dir}/dist')
    output_exe_dir = os.path.normpath(f'{toml_dir}/assets/base')
    log.log_message(f"Setting up directories: TOML dir: {toml_dir}, Dist dir: {dist_dir}, Output exe dir: {output_exe_dir}")

    os.makedirs(output_exe_dir, exist_ok=True)
    log.log_message(f"Ensured existence of directory: {output_exe_dir}")

    for exe_name in exe_names:
        log.log_message(f"Extracted executable name: {exe_name}")

        if platform.system() == 'Windows':
            dist_exe = os.path.normpath(f'{dist_dir}/{exe_name}.exe')
            final_exe_location = os.path.normpath(f'{output_exe_dir}/{exe_name}.exe')
        else:
            dist_exe = os.path.normpath(f'{dist_dir}/{exe_name}')
            final_exe_location = os.path.normpath(f'{output_exe_dir}/{exe_name}')

        log.log_message(f"Final EXE location: {final_exe_location}")

        build_exes(input_toml_path)
        log.log_message(f"Build completed for {exe_name}")

        if os.path.isfile(final_exe_location):
            log.log_message(f"Removing existing file at: {final_exe_location}")
            os.remove(final_exe_location)
        else:
            log.log_message(f"No existing file found at: {final_exe_location}")

        shutil.copy(dist_exe, final_exe_location)
        log.log_message(f"Copied EXE from {dist_exe} to {final_exe_location}")

    output_zip = os.path.normpath(f'{dist_dir}/{main_exe_name}_{os_arch_line}.zip')
    log.log_message(f"Zipping exe and related files into: {output_zip}")

    zip_directory(output_exe_dir, output_zip)
    log.log_message('Finished zipping exe and related files.')

    log.log_message(f'Executable release created at {output_zip}')

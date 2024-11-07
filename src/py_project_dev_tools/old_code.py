# import requests


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
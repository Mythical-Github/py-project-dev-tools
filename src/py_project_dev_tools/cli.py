from py_project_dev_tools import main

OPTIONS = {
    "module": main,
    "commands": {
        "clone_repo": {
            "function_name": "clone_repo",
            "arg_help_pairs": [
                {"repo_url": {
                    "help": "url of the github repo",
                    "required": True,
                    "use_nargs": False
                }},
                {"repo_branch": {
                    "help": "name of the repo branch to clone",
                    "required": True,
                    "use_nargs": False
                }},
                {"clone_recursively": {
                    "help": "if the repo should also clone its submodules",
                    "required": True,
                    "use_nargs": False
                }},
                {"output_directory": {
                    "help": "where the repository should be cloned to",
                    "required": True,
                    "use_nargs": False
                }}
            ]
        },
        "make_dev_tools_release": {
            "function_name": "make_dev_tools_release",
            "arg_help_pairs": [
                {"project_toml_path": {
                    "help": "Path to the pyproject.toml",
                    "required": True,
                    "use_nargs": False
                }}
            ]
        },
        "refresh_deps": {
            "function_name": "refresh_deps",
            "arg_help_pairs": [
                {"project_toml_path": {
                    "help": "Path to the pyproject.toml",
                    "required": True,
                    "use_nargs": False
                }}
            ]
        },
        "test_virtual_environment": {
            "function_name": "test_virtual_environment",
            "arg_help_pairs": [
                {"project_toml_path": {
                    "help": "Path to the pyproject.toml",
                    "required": True,
                    "use_nargs": False
                }}
            ]
        },
        "cleanup_repo": {
            "function_name": "cleanup_repo",
            "arg_help_pairs": [
                {"project_toml_path": {
                    "help": "Path to the pyproject.toml",
                    "required": True,
                    "use_nargs": False
                }}
            ]
        },
        "test_exe_release": {
            "function_name": "test_exe_release",
            "arg_help_pairs": [
                {"project_toml_path": {
                    "help": "Path to the pyproject.toml",
                    "required": True,
                    "use_nargs": False
                }}
            ]
        },
        "make_exe_release": {
            "function_name": "make_exe_release",
            "arg_help_pairs": [
                {"project_toml_path": {
                    "help": "Path to the pyproject.toml",
                    "required": True,
                    "use_nargs": False
                }}
            ]
        },
        "upload_latest_to_repo": {
            "function_name": "upload_latest_to_repo",
            "arg_help_pairs": [
                {"project_toml_path": {
                    "help": "Path to the pyproject.toml",
                    "required": True,
                    "use_nargs": False
                }},
                {"repo_branch": {
                    "help": "name of the repo branch to commit to",
                    "required": True,
                    "use_nargs": False
                }}
            ]
        },
        "setup_virtual_environment": {
            "function_name": "setup_virtual_environment",
            "arg_help_pairs": [
                {"project_toml_path": {
                    "help": "Path to the pyproject.toml",
                    "required": True,
                    "use_nargs": False
                }}
            ]
        },
        "zip_directory": {
            "function_name": "zip_directory",
            "arg_help_pairs": [
                {"input_dir": {
                    "help": "path of the dir to zip",
                    "required": True,
                    "use_nargs": False
                }},
                {"output_zip_file": {
                    "help": "path of the output zip",
                    "required": True,
                    "use_nargs": False
                }}
            ]
        },
        "unzip_zip": {
            "function_name": "unzip_zip",
            "arg_help_pairs": [
                {"input_zip_path": {
                    "help": "path to the zip to unzip",
                    "required": True,
                    "use_nargs": False
                }},
                {"output_files_dir": {
                    "help": "path to the folder to unzip the zip files to",
                    "required": True,
                    "use_nargs": False
                }}
            ]
        },
        "lint_code": {
            "function_name": "lint_code",
            "arg_help_pairs": [
                {"project_toml_path": {
                    "help": "Path to the pyproject.toml",
                    "required": True,
                    "use_nargs": False
                }}
            ]
        }
    }
}

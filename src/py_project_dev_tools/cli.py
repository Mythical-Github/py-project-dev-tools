from py_project_dev_tools import main

OPTIONS = {
    "module": main,
    "commands": {
        "clone_repo": {
            "function_name": "clone_repo",
            "arg_help_pairs": [
                {"repo_url": "url of the github repo"},
                {"repo_branch": "name of the repo branch to clone"},
                {"clone_recursively": "if the repo should also clone it's submodules"},
                {"output_directory": "where the repository should be cloned to"},
            ]
        },
        "make_dev_tools_release": {
            "function_name": "make_dev_tools_release",
            "arg_help_pairs": [
                {"project_toml_path": "Path to the pyproject.toml"}
            ]
        },
        "refresh_deps": {
            "function_name": "refresh_deps",
            "arg_help_pairs": [
                {"project_toml_path": "Path to the pyproject.toml"}
            ]
        },
        "test_virtual_environment": {
            "function_name": "test_virtual_environment",
            "arg_help_pairs": [
                {"project_toml_path": "Path to the pyproject.toml"}
            ]
        },
        "cleanup_repo": {
            "function_name": "cleanup_repo",
            "arg_help_pairs": [
                {"project_toml_path": "Path to the pyproject.toml"}
            ]
        },
        "test_exe_release": {
            "function_name": "test_exe_release",
            "arg_help_pairs": [
                {"project_toml_path": "Path to the pyproject.toml"}
            ]
        },
        "make_exe_release": {
            "function_name": "make_exe_release",
            "arg_help_pairs": [
                {"project_toml_path": "Path to the pyproject.toml"}
            ]
        },
        "upload_latest_to_repo": {
            "function_name": "upload_latest_to_repo",
            "arg_help_pairs": [
                {"project_toml_path": "Path to the pyproject.toml"},
                {"repo_branch": "name of the repo branch to commit to"},
            ]
        },
        "setup_virtual_environment": {
            "function_name": "setup_virtual_environment",
            "arg_help_pairs": [
                {"project_toml_path": "Path to the pyproject.toml"}
            ]
        },
        "zip_directory": {
            "function_name": "zip_dir",
            "arg_help_pairs": [
                {"input_dir": "path of the dir to zip"},
                {"output_zip_file": "path of the output zip"},
            ]
        }
    }
}

from py_project_dev_tools import main

OPTIONS = {
    "module": main,
    "commands": {
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
        "make_exe_release_ci_cd": {
            "function_name": "make_exe_release_ci_cd",
            "arg_help_pairs": [
                {"os_arch_line": {
                    "help": "The os_arch string to use for naming the release zip.",
                    "required": False,
                    "use_nargs": False
                }}
            ]
        }
    }
}
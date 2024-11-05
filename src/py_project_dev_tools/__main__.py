import sys
from pathlib import Path

from py_project_dev_tools import cli_py
from py_project_dev_tools.cli import OPTIONS
from py_project_dev_tools import log_py as log
from py_project_dev_tools.log_colors import COLORS


if getattr(sys, 'frozen', False):
    script_dir = Path(sys.executable).parent
else:
    script_dir = Path(__file__).resolve().parent

def main():
    try:
        log.set_log_base_dir(script_dir)
        log.configure_logging(COLORS)
        cli_py.cli_logic(OPTIONS)
    except Exception as error_message:
        log.log_message(str(error_message))

if __name__ == "__main__":
    main()

"""
Collection of helper methods

Methods
-------
get_header(pdf_path):
    Print a header

file_checker(file_name):
    Check for file existance and if empty

init_output_dir():
    Check for output dir
"""
from pathlib import Path

import typer
from rich import print as rprint


def get_header():
    """
    Print a header
    """
    txt = """[bold red]
    
        ▀▀█▀▀ █▀▀█ █▀▀█ █── ░█─▄▀ ─▀─ ▀▀█▀▀ 
        ──█── █▄▀█ █▄▀█ █── ░█▀▄─ ▀█▀ ─░█── 
        ──▀── █▄▄█ █▄▄█ ▀▀▀ ░█─░█ ▀▀▀ ─░█──
        [/bold red]"""
    rprint(txt)


def file_checker(file_name: Path):
    """
    Check for file existance and if empty
    """
    if file_name and file_name.is_file():
        print(f"✔️ File found: {file_name.resolve()}")
    else:
        print("⚠️ File not found. Try again")
        raise typer.Abort()


def dir_checker(file_path: Path):
    """
    Check for directory existance and if empty
    """
    if file_path and file_path.is_dir():
        if any(file_path.iterdir()):
            print(f"✔️ File(s) path found: {file_path.resolve()}")
        else:
            print("⚠️ File(s) path is empty. Try again")
            raise typer.Abort()
    else:
        print("⚠️ File(s) path not found. Try again")
        raise typer.Abort()


def file_ext_checker(file_path: Path, file_ext: str) -> bool:
    """
    Check for file extension(s) in a directory

    Only use it after checking directory existance
    """
    # Get files with ext
    paths = list(file_path.glob(f"*.{file_ext}"))

    # Return True if there's at least 1 path
    return bool(len(paths) > 0)


def init_output_dir():
    """
    Check for output dir, make dir if not found
    """
    path_checker = Path("tmp_output")

    if not path_checker.is_dir():
        path_checker.mkdir()
    else:
        pass

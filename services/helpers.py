"""
Collection of helper methods
"""
import time
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


def get_files_same_ext_path(file_path: Path, file_ext: str) -> list[Path]:
    """
    Get files with same extension paths

    Only use it after checking directory existance
    """
    # Return with ext
    return list(file_path.glob(f"*.{file_ext}"))


def file_ext_checker(file_path: Path, file_ext: str) -> bool:
    """
    Check for files with same extension in a directory

    Only use it after checking directory existance
    """
    # Get files with ext
    paths = get_files_same_ext_path(file_path, file_ext)

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


def get_unix() -> int:
    """
    Get current unix timestamp
    """
    return int(time.time())

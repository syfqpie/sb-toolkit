"""
Global helpers class
"""
from pathlib import Path

import typer
from rich import print as rprint


class Helper:
    """
    Collection of helper methods

    Methods
    -------
    header(pdf_path):
        Print a header

    file_checker(file_name):
        Check for file existance and if empty

    init_output_dir():
        Check for output dir
    """

    @staticmethod
    def header():
        """
        Print a header
        """
        txt = """[bold red]
        
            ▀▀█▀▀ █▀▀█ █▀▀█ █── ░█─▄▀ ─▀─ ▀▀█▀▀ 
            ──█── █▄▀█ █▄▀█ █── ░█▀▄─ ▀█▀ ─░█── 
            ──▀── █▄▄█ █▄▄█ ▀▀▀ ░█─░█ ▀▀▀ ─░█──
            [/bold red]"""
        rprint(txt)

    @staticmethod
    def file_checker(file_name: Path):
        """
        Check for file existance and if empty
        """
        if file_name and file_name.is_file():
            print(f"✔️ File found: {file_name.resolve()}")
        else:
            print("⚠️ File not found. Try again")
            raise typer.Abort()

    @staticmethod
    def init_output_dir():
        """
        Check for output dir, make dir if not found
        """
        path_checker = Path("tmp_output")

        if not path_checker.is_dir():
            path_checker.mkdir()
        else:
            pass

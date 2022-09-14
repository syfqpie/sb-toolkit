"""
ToolKiT by SB. Implemented using Typer
"""

from pathlib import Path

import typer
from rich.prompt import IntPrompt

from services import helpers as Helper
from services import pdf_kit as PDFKit


app = typer.Typer(no_args_is_help=True)


@app.command(no_args_is_help=True)
def pdf_split(
    file_name: Path = typer.Argument(..., help="PDF file name", metavar="🍄 file name"),
    allpage: bool = typer.Option(False, help="All pages", metavar="🍄 all pages"),
):
    """
    Split PDF into files

    """
    # Check file existance
    Helper.file_checker(file_name)
    start = None
    end = None
    step = None

    # Prompt to get info
    if not allpage:
        # Validate no to be at least 1
        while True:
            start = IntPrompt.ask("➡️ Start page")
            if start > 0:
                break
            print("⚠️ Must start with at least 1")

        end = IntPrompt.ask("➡️ End page")
        step = IntPrompt.ask("➡️ Step")

        # Validate if start > end
        if start and end and start > end:
            raise typer.BadParameter("⚠️ End page should be higher than start page")

    # Get information
    PDFKit.extract_info(file_name)

    # Split
    PDFKit.split(file_name, start, end, step)


@app.command(no_args_is_help=True)
def pdf_combine(
    files_dir: Path = typer.Argument(
        ...,
        help="PDF files directory",
        metavar="🍄 directory",
    )
):
    """
    Combine PDF into single file

    """
    # Check dir exists and not empty
    Helper.dir_checker(files_dir)

    # Check if dir contains .pdf files
    is_ext_exists = Helper.file_ext_checker(files_dir, "pdf")

    # Raise if no pdf ext
    if not is_ext_exists:
        raise typer.BadParameter("⚠️ Directory don't have any pdf file(s)")

    # Merge
    PDFKit.merge(files_dir)


if __name__ == "__main__":
    Helper.get_header()
    app()

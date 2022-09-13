"""
ToolKiT by SB. Implemented using Typer
"""

from pathlib import Path

import typer
from rich.prompt import IntPrompt

from services.helpers import file_checker, dir_checker, file_ext_checker, get_header
from services.pdf_kit import PDFKit


app = typer.Typer()


@app.command(no_args_is_help=True)
def pdf_split(
    file_name: Path = typer.Argument(..., help="PDF file name", metavar="🍄 file name"),
    allpage: bool = typer.Option(False, help="All pages", metavar="🍄 all pages"),
):
    """
    Split PDF into files

    """
    # Check file existance
    file_checker(file_name)
    start = None
    end = None
    step = None

    # Prompt to get info
    if not allpage:
        start = IntPrompt.ask("➡️ Start page")
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
    dir_checker(files_dir)

    # Check if dir contains .pdf files
    is_ext_exists = file_ext_checker(files_dir, "pdf")

    # Raise if no pdf ext
    if not is_ext_exists:
        raise typer.BadParameter("⚠️ Directory don't have any pdf file(s)")

    # Merge
    PDFKit.merge(files_dir)


if __name__ == "__main__":
    get_header()
    app()

import typer

from pathlib import Path
from typing import Optional
from rich.prompt import Prompt, IntPrompt

from services.helpers import Helper
from services.pdf_kit import PDFKit


app = typer.Typer()


@app.command(no_args_is_help=True)
def pdf_split(file_name: Path = typer.Argument(..., help='PDF file name', metavar='🍄 file name'),
    all: bool = typer.Option(False, help='All pages', metavar='🍄 all pages')):
    '''
    Split PDF into files
    '''
    # Check file existance
    Helper.file_checker(file_name)
    start = None
    end = None
    step = None

    # Prompt to get info
    if not all:
        start = IntPrompt.ask('➡️ Start page')
        end = IntPrompt.ask('➡️ End page')
        step = IntPrompt.ask('➡️ Step')

        # Validate if start > end
        if start and end and start > end:
            raise typer.BadParameter(
                f'⚠️ End page should be higher than start page'
            )

    # Get information
    PDFKit.extract_info(file_name)

    # Split
    PDFKit.split(file_name, start, end, step)



if __name__ == '__main__':
    Helper.header()
    app()


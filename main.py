import typer

from pathlib import Path
from typing import Optional

from services.helpers import Helper
from services.pdf_kit import PDFKit


app = typer.Typer()


@app.command()
def pdf_split(
    file_name: Optional[Path] = typer.Option(None),
    start: Optional[int] = typer.Option(None),
    end: Optional[int] = typer.Option(None),
    step: Optional[int] = typer.Option(None)):
    # Check file existance
    Helper.file_checker(file_name)

    # Validate if start > end
    if start and end and start > end:
        raise typer.BadParameter(
            f'End page should be higher than start page'
        )

    # Get information
    PDFKit.extract_info(file_name)

    # Split
    PDFKit.split(file_name, start, end, step)

if __name__ == '__main__':
    app()


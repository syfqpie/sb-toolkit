"""
Tools for PDF

Methods
-------
extract_info(pdf_path):
    Extract info from PDF file

split(pdf_path, start, end, step):
    Split PDF to pages

merge(dir_path):
    Merge pdfs in a directory
"""
from pathlib import Path

import typer
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from rich.progress import track

from . import helpers as Helper


def extract_info(pdf_path: Path):
    """
    Extract info from PDF file

        Parameters:
            pdf_path (Path) : PDF file path with file name
    """
    with open(pdf_path, "rb") as opened_file:
        pdf = PdfFileReader(opened_file)
        info = pdf.getDocumentInfo()
        no_of_pages = pdf.getNumPages()

    txt = f"""
        Information about { pdf_path }: 

        Author: { info.author }
        Creator: { info.creator }
        Producer: { info.producer }
        Subject: { info.subject }
        Title: { info.title }
        Number of pages: { no_of_pages }
    """

    print(txt)
    return info


def split(pdf_path: Path, start: int = None, end: int = None, step: int = None):
    """
    Split PDF to pages. If start, end, step is not given all
    pages will be splitted

        Parameters:
            pdf_path (Path) : PDF file path with file name
            start    (int)  : Start page
            end      (int)  : End page
            step     (int)  : Step
    """
    # Init output folder first
    Helper.init_output_dir()

    # Validate end
    pdf = PdfFileReader(pdf_path)
    no_of_pages = pdf.getNumPages()

    if end and no_of_pages < end:
        raise typer.BadParameter(
            f"⚠️ End page should be within { 1 if start is None else start } - { no_of_pages }"
        )

    # Get variables
    start_index = 0 if start is None else start - 1
    end_index = no_of_pages if end is None else end
    stepper = 1 if step is None or step == 0 else step
    total = 0

    # Split
    for page in track(
        range(start_index, end_index, stepper), description="⌚ Splitting..."
    ):
        # Init file writer and add page
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        # Name output and write
        output = f"tmp_output/splitted_{ page + 1 }.pdf"
        with open(output, "wb") as output_pdf:
            pdf_writer.write(output_pdf)

        # Update counter and close file
        total += 1
        output_pdf.close()

    print(f"✔️ Splitted to { total } files.")


def merge(dir_path: Path):
    """
    Merge pdfs in a directory

        Parameters:
            dir_path (Path) : PDF files path
    """
    # Init output folder first
    Helper.init_output_dir()
    paths = Helper.get_files_same_ext_path(dir_path, "pdf")
    merger = PdfFileMerger()

    # Append pages
    for pat in paths:
        with open(pat, "rb") as curr_file:
            merger.append(curr_file)
        curr_file.close()

    # Write to output doc
    with open("tmp_output/merged.pdf", "wb") as output_pdf:
        merger.write(output_pdf)

    # Close files
    merger.close()
    output_pdf.close()

    print("✔️ Files merged")

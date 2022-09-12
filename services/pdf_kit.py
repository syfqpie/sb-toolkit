import typer

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

from services.helpers import Helper

class PDFKit():
    '''
        Tools for PDF
    '''
    def extract_info(pdf_path: Path):
        with open(pdf_path, 'rb') as f:
            pdf = PdfFileReader(f)
            info = pdf.getDocumentInfo()
            no_of_pages = pdf.getNumPages()

        txt = f'''
            Information about { pdf_path }: 

            Author: { info.author }
            Creator: { info.creator }
            Producer: { info.producer }
            Subject: { info.subject }
            Title: { info.title }
            Number of pages: { no_of_pages }
        '''

        print(txt)
        return info
    
    def split(pdf_path: Path, start: int = None, end: int = None, step: int = None):
        # Init output folder first
        Helper.init_output_dir()

        # Validate end
        pdf = PdfFileReader(pdf_path)
        no_of_pages = pdf.getNumPages()

        # Validate end page
        if end and no_of_pages < end:
            raise typer.BadParameter(
                f'End page should be within { 1 if start == None else start } - { no_of_pages }'
            )

        # Get variables
        start_index = 0 if start == None else start - 1
        end_index = no_of_pages if end == None else end
        stepper = 1 if step == None or step == 0 else step

        # Split
        for page in range(start_index, end_index, stepper):
            print(f'✔️ Page: { page + 1 }')
            # pdf_writer = PdfFileWriter()
            # pdf_writer.addPage(pdf.getPage(page))

            # output = f'tmp_output/splitted_{ page + 1 }.pdf'
            # with open(output, 'wb') as output_pdf:
            #     pdf_writer.write(output_pdf)
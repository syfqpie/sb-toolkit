import typer

from pathlib import Path
from typing import Optional


app = typer.Typer()

class PDFKit():
    pass


@app.command()
def pdf_split(file_name: Optional[Path] = typer.Option(None)):
    
    if file_name:
        try:
            is_file = file_name.is_file()
            if not is_file:
                raise FileNotFoundError
            else:
                print(f'✔️ File found: {file_name.resolve()}')
        except FileNotFoundError:
            print('⚠️ File not found. Try again')
            raise typer.Abort()
    else:
        print('⚠️ Please enter filename')
        raise typer.Abort()
    

if __name__ == '__main__':
    app()


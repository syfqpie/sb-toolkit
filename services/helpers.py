import typer
from pathlib import Path
from rich import print as rprint


class Helper():
    @staticmethod
    def header():
        txt = f'''[bold red]
        
            ▀▀█▀▀ █▀▀█ █▀▀█ █── ░█─▄▀ ─▀─ ▀▀█▀▀ 
            ──█── █▄▀█ █▄▀█ █── ░█▀▄─ ▀█▀ ─░█── 
            ──▀── █▄▄█ █▄▄█ ▀▀▀ ░█─░█ ▀▀▀ ─░█──
            [/bold red]'''
        rprint(txt)

    @staticmethod
    def file_checker(file_name: Path):
        '''
            Check for file existance and if empty
        '''
        if file_name and file_name.is_file():
            print(f'✔️ File found: {file_name.resolve()}')
        else:
            print('⚠️ File not found. Try again')
            raise typer.Abort()
    
    @staticmethod
    def init_output_dir():
        path_checker = Path('tmp_output')

        if not path_checker.is_dir():
            path_checker.mkdir()
        else:
            pass
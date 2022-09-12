import typer
from pathlib import Path


class Helper():
    @staticmethod
    def file_checker(file_name: Path):
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
    
    @staticmethod
    def init_output_dir():
        path_checker = Path('tmp_output')

        if not path_checker.is_dir():
            path_checker.mkdir()
        else:
            pass
import os
import typer
from .utils import error_message
from .pdf_handler import file_pdf, url_pdf

app = typer.Typer(add_completion=False)


@app.command('github')
def github():
    """open github repo for Kiki"""

    typer.echo('Opening GitHub Repo...')
    typer.launch('https://github.com/VijayStroup/Kiki')


@app.command('get')
def get(
    pdf: str = typer.Argument(..., help='url or file of pdf'),
    filename: str = typer.Option('kiki', help='name of output file without extension')
):
    """get audio from pdf"""

    # check to make sure pdf arg is a pdf file
    if not pdf[-3:] == 'pdf':
        error_message(f"Invalid file '{pdf}'. Must be a pdf file.")

    # check if pdf is file or url
    if os.path.isfile(pdf):
        file_pdf(pdf, filename)
    else:
        url_pdf(pdf, filename)

    typer.echo(f'Your audio file is now available at {filename}.mp3')


def main():
    app()

import os
import typer
from utils import error_message
import pdf_handler as pdfh


def main(
    pdf: str = typer.Argument(..., help='url or file of pdf'),
    filename: str = typer.Option('kiki', help='name of output file without extension')
):
    """
    Kiki\n
    Example Documentation
    """

    # check to make sure pdf arg is a pdf file
    if not pdf[-3:] == 'pdf':
        error_message(f"Invalid file '{pdf}'. Must be a pdf file.")

    # check if pdf is file or url
    if os.path.isfile(pdf):
        pdfh.file_pdf(pdf, filename)
    else:
        pdfh.url_pdf(pdf, filename)

    typer.echo(f'Your audio file is now available at {filename}.mp3')


if __name__ == '__main__':
    typer.run(main)

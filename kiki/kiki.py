import os
import typer


def error_message(description: str):
    typer.echo(f'Usage: kiki.py [OPTIONS] PDF\nTry \'kiki.py --help\' for help.\n\n{description}')


def main(
    pdf: str = typer.Argument(..., help='url or file of pdf'),
    filename: str = typer.Option('pdf', help='name of output file without extension')
):
    """
    Kiki\n
    Example Documentation
    """

    # check to make sure pdf arg is a pdf file
    if not pdf[-3:] == 'pdf':
        error_message(f'Error: Invalid file \'{pdf}\'. Must be a pdf file.')
        raise typer.Exit()

    # check if pdf is file or url
    if os.path.isfile(pdf):
        typer.echo(f'{pdf} is a file')
    else:
        typer.echo(f'{pdf} is not file')


if __name__ == '__main__':
    typer.run(main)

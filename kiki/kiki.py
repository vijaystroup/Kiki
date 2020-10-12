import os
import typer


def main(
    pdf: str = typer.Argument(..., help='url or file of pdf'),
    filename: str = typer.Option('pdf', help='name of output file without extension')
):
    """
    Kiki\n
    Example Documentation
    """

    # check if pdf is file or url
    if os.path.isfile(pdf):
        typer.echo(f'{pdf} is a file')
    else:
        typer.echo(f'{pdf} is not file')


if __name__ == '__main__':
    typer.run(main)

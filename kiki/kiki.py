import typer


def main(
    pdf: str = typer.Argument(..., help='url or file of pdf'),
    filename: str = typer.Option('pdf', help='name of output file without extension')
):
    """
    Kiki\n
    Example Documentation
    """

    typer.echo(f'PDF: {pdf}\tFILENAME: {filename}')


if __name__ == '__main__':
    typer.run(main)

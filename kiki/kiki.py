import typer


def main(
    name: str = typer.Argument(...)
):
    """
    Kiki\n
    Example Documentation
    """

    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)

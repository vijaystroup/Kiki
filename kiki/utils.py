from typer import echo, Exit


def error_message(description):
    echo(f"Usage: kiki.py [OPTIONS] PDF\nTry 'kiki.py --help' for help.\n\nError: {description}")
    raise Exit()

from typer import echo


def error_message(description):
    echo(f"Usage: kiki.py [OPTIONS] PDF\nTry 'kiki.py --help' for help.\n\nError: {description}")
    exit(-1)

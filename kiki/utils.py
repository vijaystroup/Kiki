from typer import echo, style, colors


def error_message(description):
    error = style(description, fg=colors.RED)
    echo(f"Usage: kiki.py [OPTIONS] PDF\nTry 'kiki.py --help' for help.\n\nError: {error}")
    exit(-1)

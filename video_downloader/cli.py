"""Command Line Interface Video Downloader"""

import typer
from typer import Typer

app = Typer(help=__doc__)


@app.command()
def hello():
    """simple docstring"""
    typer.echo("Hello World")


@app.command()
def goodbye():
    """simple docstring"""
    typer.echo("Good bye")


def entry_point():  # pragma: no cover
    """entry point"""
    app()

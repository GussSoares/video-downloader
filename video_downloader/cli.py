import typer
from typer import Typer


app = Typer()


@app.command()
def hello():
    """simple docstring"""
    typer.echo("Hello Moto")


@app.command()
def goodbye():
    """simple docstring"""
    typer.echo("Good bye")


@app.callback(invoke_without_command=True)
def main(url: str):
    """simple docstring"""
    typer.echo(url)



def entry_point():
    app()

import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """A Python CLI for adding pre-defined topics to a GitHub repository."""
    click.echo("Hello, world!")

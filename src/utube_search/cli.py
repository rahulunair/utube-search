"""cli to github peek."""

from rich import print as rprint
from rich.console import Console
from rich.table import Table
import typer

from utube_search.api import main
from utube_search.exceptions import YtsException


app = typer.Typer()


@app.command()
def search(query: str, cache: bool = True, kind="table"):
    """search for videos with query on youtube."""
    try:
        typer.secho(f"searching for videos: {query}...", fg=typer.colors.GREEN)
        if kind == "json":
            content = main(query, cache, kind="json")
            rprint(content)
        elif kind == "table":
            content = main(query, False, kind="list")
            table = Table(title="Search Results")
            table.add_column("Title", justify="right", style="cyan", no_wrap=False)
            table.add_column("Video URL", style="magenta", no_wrap=True)
            table.add_column("Duration", style="green")
            table.add_column("View count", style="green")
            table.add_column("Published Time", style="green")
            for c in content:
                table.add_row(
                    " ".join(c["title"].split(" ")[:4]),
                    c["url"],
                    c["duration"],
                    str(c["view_count"]),
                    c["publish_time"],
                )
            console = Console()
            console.print(table)
    except YtsException:
        typer.echo("internal API raised an exception")
        raise typer.Abort()
    except YtsException:
        typer.echo("failed to get response from youtube")
        raise typer.Abort()


@app.command()
def info():
    """information about the tool."""
    typer.secho("a cli tool to search youtube.")
    # typer.secho("version: {}".format(__version__))


if __name__ == "__main__":
    app()

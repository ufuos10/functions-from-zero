from mylib.bot import get_summary
import click


@click.command()
@click.option(
    "--title",
    prompt="Enter a Wikipedia page title",
    help="The title of the Wikipedia page to summarize.",
)
def scrape(title):
    summary = get_summary(title)
    if summary is None:
        click.echo(f"No page found for '{title}'.")
        return

    click.secho(summary, fg="green")


if __name__ == "__main__":
    scrape()  # pylint: disable=no-value-for-parameter
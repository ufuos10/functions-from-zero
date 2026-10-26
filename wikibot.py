import wikipediaapi
import click

wiki = wikipediaapi.Wikipedia(
    user_agent="LearningApp/1.0 (masoncute4real@gmail.com)",
    language="en",
)

@click.command()
@click.option('--title', prompt='Enter a Wikipedia page title', help='The title of the Wikipedia page to summarize.')



def get_summary(title):
    page = wiki.page(title)
    if not page.exists():
        click.echo(f"No page found for '{title}'.")
        return

    sentences = page.summary.split(". ")
    click.secho(". ".join(sentences[:2]) + ".", bg="white", fg="green")

if __name__ == "__main__":
    get_summary() # pylint: disable=no-value-for-parameter

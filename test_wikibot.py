from click.testing import CliRunner
from mylib.bot import get_summary
from wikibot import scrape

def test_get_summary():
    assert "Microsoft" in get_summary("Microsoft")

def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(scrape, ["--title", "Microsoft"])
    assert result.exit_code == 0
    assert "Microsoft" in result.output

from click.testing import CliRunner
from wikibot import get_summary


def test_get_summary():
    runner = CliRunner()
    result = runner.invoke(get_summary, ["--title", "Microsoft"])
    assert result.exit_code == 0
    assert "Microsoft" in result.output
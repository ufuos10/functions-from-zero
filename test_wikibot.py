from wikibot import get_summary

def test_get_summary():
    assert "Microsoft" in get_summary("Microsoft")
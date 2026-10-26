import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    user_agent="LearningApp/1.0 (masoncute4real@gmail.com)",
    language="en",
)


def get_summary(title, sentence_count=2):
    """Return the first few sentences of a Wikipedia page, or None if not found."""
    page = wiki.page(title)
    if not page.exists():
        return None

    sentences = page.summary.split(". ")
    return ". ".join(sentences[:sentence_count]) + "."
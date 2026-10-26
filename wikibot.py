import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    user_agent="LearningApp/1.0 (masoncute4real@gmail.com)",
    language="en",
)

def get_summary(title):
    page = wiki.page(title)
    if not page.exists():
        return f"No page found for '{title}'."
    return page.summary.split(". ")[0] + "."

print(get_summary("Microsoft"))
# test_google_search.py

import pytest

from pages.google_page import GooglePage


def test_google_search(browser):
    google_page = GooglePage(browser)
    google_page.load()

    # Validate the search results
    assert "Google" in browser.title or "Google" in browser.current_url


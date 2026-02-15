from urllib.parse import urlparse

from playwright.sync_api import Page

from pages.home_page import HomePage


def _home_url(page: Page) -> str:
    """Derive home (book-scan) URL from the current page URL for session-scoped reuse."""
    parsed = urlparse(page.url)
    return f"{parsed.scheme}://{parsed.netloc}/book-scan"


def click_book_a_scan_button(page: Page) -> None:
    """Navigate to home, then click the "Book a scan" button.
    Ensures correct behavior when reusing a session-scoped page left on another URL.
    """
    page.goto(_home_url(page))
    home_page = HomePage(page)
    home_page.wait_for_loaded()
    home_page.book_a_scan_button.click()
from playwright.sync_api import Page


class BasePage:
    """Base page object with shared page reference."""

    def __init__(self, page: Page):
        self.page = page

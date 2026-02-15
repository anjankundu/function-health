from playwright.sync_api import Page

from pages.base import BasePage


class HomePage(BasePage):
    """Page object for the home page"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_title = self.page.locator(".section-header").first
        self.book_a_scan_button = self.page.get_by_role("button", name="Book a scan")
        self.sign_out_button =  self.page.get_by_role("button", name="Sign out")

    def wait_for_loaded(self) -> None:
        """Wait until the home page is fully loaded."""
        self.page_title.wait_for(state="visible")

    def sign_out(self) -> None:
        """Click sign out if the button is visible."""
        if self.sign_out_button.is_visible():
            self.sign_out_button.click()

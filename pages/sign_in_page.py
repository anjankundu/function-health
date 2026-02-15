from playwright.sync_api import Page

from pages.base import BasePage


class SignInPage(BasePage):
    """Page object for the sign-in page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.email_textbox = self.page.get_by_role("textbox", name="Email")
        self.password_textbox = self.page.get_by_role("textbox", name="Password")
        self.accept_button = self.page.get_by_role("button", name="Accept")
        self.submit_button = self.page.get_by_role("button", name="Submit")

    def login(self, login_url: str, username: str, password: str) -> None:
        """Navigate to sign-in, accept cookies, and submit credentials."""
        self.page.goto(login_url)
        self.email_textbox.wait_for(state="visible")
        self.accept_button.click()
        self.email_textbox.fill(username)
        self.password_textbox.fill(password)
        self.submit_button.click()

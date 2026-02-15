from playwright.sync_api import Page

from pages.base import BasePage


class SelectScanPage(BasePage):
    """Page object for the "Select your scan" page"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_title = self.page.locator(".title-container h4")
        self.date_of_birth = self.page.get_by_role(
            "textbox", name="Date of birth (MM-DD-YYYY)"
        )
        self.sex = self.page.get_by_role("combobox")
        self.sex_male = self.page.get_by_text("Male", exact=True)
        self.sex_female = self.page.get_by_text("Female", exact=True)
        self.scan_type = self.page.locator(".encounter-card")
        self.continue_button = self.page.get_by_test_id("select-plan-submit-btn")

    def wait_for_loaded(self) -> None:
        """Wait until "Select your scan" page is fully loaded."""
        self.continue_button.wait_for(state="visible")

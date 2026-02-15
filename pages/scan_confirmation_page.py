from playwright.sync_api import Page

from pages.base import BasePage


class ScanConfirmationPage(BasePage):
    """Page object for the "Scan confirmation" page"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.begin_medical_questionnaire_button = self.page.get_by_role("button", name="Begin Medical Questionnaire")

    def wait_for_loaded(self) -> None:
        """Wait until "Scan confirmation" page is fully loaded."""
        self.begin_medical_questionnaire_button.wait_for(state="visible")
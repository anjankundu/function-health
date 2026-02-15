from playwright.sync_api import Page

from pages.base import BasePage


class ScheduleScanPage(BasePage):
    """Page object for the "Schedule your scan" page"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.appointment_location = self.page.locator(".location-card")
        self.appointment_date = self.page.locator(".vuecal__cell:not(.vuecal__cell--disabled)")
        self.appointment_time = self.page.locator(".datepicker .appointments__individual-appointment")
        self.continue_button = self.page.locator("[data-test='submit']")
    
    def wait_for_loaded(self) -> None:
        """Wait until "Schedule your scan" page is fully loaded."""
        self.continue_button.wait_for(state="visible")
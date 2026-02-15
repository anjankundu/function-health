from pages.schedule_scan_page import ScheduleScanPage
from playwright.sync_api import Page


def fill_and_submit_schedule_scan_page(page: Page) -> None:
    """Navigate through "Schedule your scan" page, fill fields and submit."""
    schedule_scan_page = ScheduleScanPage(page)
    schedule_scan_page.wait_for_loaded()

    schedule_scan_page.appointment_location.first.click()
    schedule_scan_page.appointment_date.first.click()
    schedule_scan_page.appointment_time.first.scroll_into_view_if_needed()
    schedule_scan_page.appointment_time.first.click()
    schedule_scan_page.continue_button.click()

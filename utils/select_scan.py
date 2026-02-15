from playwright.sync_api import Page

from pages.select_scan_page import SelectScanPage
from utils.enums import SelectScanPageDefaults


def fill_and_submit_select_scan_page(page: Page) -> None:
    """Navigate through "Select your scan" page, fill fields and submit."""
    select_scan_page = SelectScanPage(page)
    select_scan_page.wait_for_loaded()

    if select_scan_page.date_of_birth.is_visible():
        select_scan_page.date_of_birth.click()
        select_scan_page.date_of_birth.fill(SelectScanPageDefaults.DATE_OF_BIRTH)
        select_scan_page.sex.click()
        select_scan_page.sex_female.first.click()

    select_scan_page.scan_type.first.click()
    select_scan_page.continue_button.click()

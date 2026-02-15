from pages.reserve_appointment_page import ReserveAppointmentPage
from playwright.sync_api import Page

from utils.enums import ReserveAppointmentPageDefaults


def fill_and_submit_reserve_appointment_page(page: Page) -> None:
    """Navigate through "Reserve your appointment" page, fill fields and submit."""
    reserve_appointment_page = ReserveAppointmentPage(page)
    reserve_appointment_page.wait_for_loaded()

    reserve_appointment_page.credit_card_number.fill(
        ReserveAppointmentPageDefaults.CREDIT_CARD_NUMBER
    )
    reserve_appointment_page.credit_card_expiration_date.fill(
        ReserveAppointmentPageDefaults.CREDIT_CARD_EXPIRATION_DATE
    )
    reserve_appointment_page.credit_card_security_code.fill(
        ReserveAppointmentPageDefaults.CREDIT_CARD_SECURITY_CODE
    )
    reserve_appointment_page.credit_card_zip_code.fill(
        ReserveAppointmentPageDefaults.CREDIT_CARD_ZIP_CODE
    )
    reserve_appointment_page.continue_button.click()

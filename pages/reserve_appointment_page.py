from playwright.sync_api import Page

from pages.base import BasePage


class ReserveAppointmentPage(BasePage):
    """Page object for the "Reserve your appointment" page.
    Payment form uses Stripe Elements - card inputs are inside Stripe iframes.
    """

    # Stripe iframe names are dynamic (e.g. __privateStripeFrame00413); use prefix match
    _STRIPE_FRAME = 'iframe[name^="__privateStripeFrame"]'

    def __init__(self, page: Page):
        super().__init__(page)
        stripe = self.page.frame_locator(self._STRIPE_FRAME).first
        self.credit_card_number = stripe.get_by_role("textbox", name="Card number")
        self.credit_card_expiration_date = stripe.get_by_role(
            "textbox", name="Expiration date MM / YY"
        )
        self.credit_card_security_code = stripe.get_by_role(
            "textbox", name="Security code"
        )
        self.credit_card_zip_code = stripe.get_by_role("textbox", name="ZIP code")
        self.continue_button = self.page.locator("[data-test='submit']")

    def wait_for_loaded(self) -> None:
        """Wait until "Reserve your appointment" page and Stripe payment form are fully loaded."""
        self.continue_button.wait_for(state="visible")

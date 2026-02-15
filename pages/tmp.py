import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://myezra-staging.ezra.com/sign-in")
    page.get_by_role("button", name="Accept").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("anjan@gmail.com")
    page.get_by_role("textbox", name="Email").press("Tab")
    page.get_by_role("textbox", name="Password").fill("My_password")
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("button", name="Book a scan").click()
    page.get_by_text("MRI Scan Available at $999 Scans for hundreds of potential conditions including").click()
    page.get_by_test_id("select-plan-submit-btn").click()
    page.get_by_text("Recommended AMRIC0.9 miNew").click()
    page.get_by_test_id("2-24-cal-day-content").click()
    page.get_by_text(":00 PM").first.click()
    page.locator("[data-test=\"submit\"]").click()
    page.locator("iframe[name=\"__privateStripeFrame00413\"]").content_frame.get_by_role("textbox", name="Card number").click()
    page.locator("iframe[name=\"__privateStripeFrame00413\"]").content_frame.get_by_role("textbox", name="Card number").click()
    page.locator("iframe[name=\"__privateStripeFrame00413\"]").content_frame.get_by_role("textbox", name="Card number").click()
    page.get_by_text("Back Continue").click()
    page.get_by_text("Reserve your appointmentComplete payment to secure your appointment.Choose a").click()
    page.locator("iframe[name=\"__privateStripeFrame00413\"]").content_frame.locator("div").filter(has_text=re.compile(r"^Expiration date MM / YY$")).first.click()
    page.locator("iframe[name=\"__privateStripeFrame00413\"]").content_frame.get_by_role("textbox", name="Card number").click()
    page.locator("iframe[name=\"__privateStripeFrame00413\"]").content_frame.get_by_role("textbox", name="Card number").click()
    page.locator("[data-test=\"submit\"]").click()
    page.locator("iframe[name=\"__privateStripeFrame00413\"]").content_frame.get_by_role("textbox", name="Card number").click()
    page.locator("iframe[name=\"__privateStripeFrame00413\"]").content_frame.get_by_role("textbox", name="Card number").click()
    page.locator("iframe[name=\"__privateStripeFrame00413\"]").content_frame.get_by_role("textbox", name="Card number").click()
    page.locator("iframe[name=\"__privateStripeFrame00413\"]").content_frame.get_by_role("textbox", name="Card number").click()
    page.locator("iframe[name=\"__privateStripeFrame00413\"]").content_frame.get_by_role("textbox", name="Card number").fill("4242 4242 4242 4242")
    page.locator("iframe[name=\"__privateStripeFrame00413\"]").content_frame.get_by_role("textbox", name="Expiration date MM / YY").fill("01 / 29")
    page.locator("iframe[name=\"__privateStripeFrame00413\"]").content_frame.get_by_role("textbox", name="Security code").fill("123")
    page.locator("iframe[name=\"__privateStripeFrame00413\"]").content_frame.get_by_role("textbox", name="ZIP code").fill("12345")
    page.locator("[data-test=\"submit\"]").click()
    page.goto("https://myezra-staging.ezra.com/sign-up/scan-confirm")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

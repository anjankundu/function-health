import pytest
from playwright.sync_api import expect

from pages.select_scan_page import SelectScanPage
from pages.schedule_scan_page import ScheduleScanPage
from pages.reserve_appointment_page import ReserveAppointmentPage
from pages.scan_confirmation_page import ScanConfirmationPage
from utils.home import click_book_a_scan_button
from utils.select_scan import fill_and_submit_select_scan_page
from utils.schedule_scan import fill_and_submit_schedule_scan_page
from utils.reserve_appointment import fill_and_submit_reserve_appointment_page

@pytest.mark.high
def test_book_a_scan_button(ui_login):
    """
    Click "Book a scan" button
    Verify "Select your plan" page loaded
    """
    click_book_a_scan_button(ui_login)
    select_scan_page = SelectScanPage(ui_login)
    expect(select_scan_page.continue_button).to_be_visible()


@pytest.mark.critical
def test_fill_and_submit_select_scan_page(ui_login):
    """
    Click "Book a scan" button
    Navigate through "Select your scan" page, fill fields and submit
    Verify "Schedule your plan" page loaded
    """
    click_book_a_scan_button(ui_login)
    fill_and_submit_select_scan_page(ui_login)
    schedule_scan_page = ScheduleScanPage(ui_login)
    expect(schedule_scan_page.continue_button).to_be_visible()


@pytest.mark.critical
def test_fill_and_submit_schedule_scan_page(ui_login):
    """
    Click "Book a scan" button
    Navigate through "Select your scan" page, fill fields and submit
    Navigate through "Schedule your scan" page, fill fields and submit
    Verify "Reserve your appointment" page loaded
    """
    click_book_a_scan_button(ui_login)
    fill_and_submit_select_scan_page(ui_login)
    fill_and_submit_schedule_scan_page(ui_login)
    reserve_appointment_page = ReserveAppointmentPage(ui_login)
    expect(reserve_appointment_page.continue_button).to_be_visible()


@pytest.mark.critical
def test_fill_and_submit_reserve_appointment_page(ui_login):
    """
    Click "Book a scan" button
    Navigate through "Select your scan" page, fill fields and submit
    Navigate through "Schedule your scan" page, fill fields and submit
    Navigate through "Reserve your appointment" page, fill fields and submit.
    Verify "Scan confirmation" page loaded
    """
    click_book_a_scan_button(ui_login)
    fill_and_submit_select_scan_page(ui_login)
    fill_and_submit_schedule_scan_page(ui_login)
    fill_and_submit_reserve_appointment_page(ui_login)
    scan_confirmation_page = ScanConfirmationPage(ui_login)
    scan_confirmation_page.wait_for_loaded()
    expect(scan_confirmation_page.begin_medical_questionnaire_button).to_be_visible()

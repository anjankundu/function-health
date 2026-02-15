import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.sign_in_page import SignInPage

load_dotenv()


def pytest_addoption(parser):
    """Register custom command-line options for login (optional overrides)."""
    parser.addoption(
        "--login-url",
        help="Full URL of the sign-in page (overrides LOGIN_URL env var).",
    )
    parser.addoption(
        "--username",
        help="Login email (overrides LOGIN_USERNAME env var).",
    )
    parser.addoption(
        "--password",
        help="Login password (overrides LOGIN_PASSWORD env var).",
    )


def _get_required_value(
    request: pytest.FixtureRequest, cli_name: str, env_name: str
) -> str:
    """Get configuration from environment (preferred) or CLI, failing clearly if missing."""
    value = os.getenv(env_name)
    if value:
        return value

    value = request.config.getoption(cli_name)
    if value:
        return value

    raise RuntimeError(
        f"Missing required config for {env_name}. "
        f"Set it in your .env file or pass {cli_name} on the command line."
    )


@pytest.fixture
def ui_login(page: Page, request: pytest.FixtureRequest) -> Page:
    """Log in to the app and yield the page for test use."""
    login_url = _get_required_value(request, "--login-url", "LOGIN_URL")
    username = _get_required_value(request, "--username", "LOGIN_USERNAME")
    password = _get_required_value(request, "--password", "LOGIN_PASSWORD")

    sign_in_page = SignInPage(page)
    sign_in_page.login(login_url, username, password)

    home_page = HomePage(page)
    home_page.wait_for_loaded()

    yield page

    home_page.sign_out()

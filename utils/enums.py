from enum import Enum


class SelectScanPageDefaults(str, Enum):
    """Default values used in "Select a scan" page"""

    DATE_OF_BIRTH = "01-02-1980"


class ReserveAppointmentPageDefaults(str, Enum):
    """Default values used in "Reserve your appointment" page"""

    CREDIT_CARD_NUMBER = "4242 4242 4242 4242"
    CREDIT_CARD_EXPIRATION_DATE = "01 / 29"
    CREDIT_CARD_SECURITY_CODE = "123"
    CREDIT_CARD_ZIP_CODE = "12345"

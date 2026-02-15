# Function Health Automation

## Overview
Smoke tests for Function Health booking flow.

## Tests implemented
* Click **Book a scan** button
* Navigate through **Select your scan** page, fill fields and submit
* Navigate through **Schedule your scan** page, fill fields and submit
* Navigate through **Reserve your appointment** page, fill fields and submit


## Getting Started

### 1. Install **uv**
```bash
pip install uv
```

### 2. Install dependencies
```bash
uv sync
```

### 3. Install the required browsers
```bash
uv run playwright install
```

### 4. Copy the environment example file to environment file
```bash
cp .env.example .env
```

### 5. Update the configuration variables in .env
* LOGIN_URL
* LOGIN_USERNAME
* LOGIN_PASSWORD


## Run automation

### Run all smoke tests headless
```bash
uv run pytest tests/test_smoke.py
```

### Run all smoke tests in chrome browser
```bash
uv run pytest --headed --browser-channel chrome tests/test_smoke.py
```

### Run one of the smoke tests
```bash
uv run pytest tests/test_smoke.py::test_fill_and_submit_reserve_appointment_page
```

### Run tests passing command line parameters
```bash
uv run pytest tests/test_smoke.py --LOGIN_URL=https://myezra-staging.ezra.com/ --LOGIN_USERNAME=your_email@example.com LOGIN_PASSWORD=your_password_here
```

### Run tests from pytest.ini 
```bash
# Uncomment any line in pytest.ini
uv run pytest
```

## Automation stack:
* Python
* Pytest
* Playwright


## Future roadmap:
* The current implementation defines the fixture scope as function, resulting in the teardown being executed after each individual test. Update the fixture to use a session scope so that the teardown is performed only once, after the completion of all tests within the session.
* Some configuration values, such as the scan type selection, are currently hardcoded in the implementation. To enhance scalability and maintainability, refactor the design to define these values as enums or accept them as input parameters. 
* Proceed with automation of test cases in order of defined priority.



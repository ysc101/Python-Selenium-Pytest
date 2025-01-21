# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    # Set up the Chrome WebDriver
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode for faster testing
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--window-size=1920,1080")

    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver  # This is where the tests will run

    driver.quit()  # Clean up after the tests

# google_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GooglePage:
    def __init__(self, driver):
        self.driver = driver


    def load(self):
        self.driver.get("https://www.google.co.in/")




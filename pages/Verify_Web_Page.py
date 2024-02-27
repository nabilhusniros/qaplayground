"""
This module contains a class called QaPlayground that automates interactions with the QaPlayground website using Selenium WebDriver.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class QaPlayground:

    # URL
    URL = 'https://qaplayground.dev/'

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Print Header
    def print_header(self):
        print('Header is present')

    # Intercation Methods
    def load(self):
        self.print_header()
        self.browser.get(self.URL)
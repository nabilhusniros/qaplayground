from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class QaPlayground:

    # URL
    URL = 'https://qaplayground.dev/'

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Intercation Methods
    def load(self):
        self.browser.get(self.URL)
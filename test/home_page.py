"""
This module is to verify the homepage is displayed
"""

from pages.qa_playground import QaPlayground
from selenium.webdriver.common.by import By

def test_homepage_display(browser):
    home_page = QaPlayground(browser)

    # Given the qaplayground home page is displayed
    home_page.load()

    # And the browser title is 'Playground for the QA automation engineers'
    assert "Playground for the QA automation engineers" in browser.title
"""
This module is to verify the homepage is displayed
"""

from pages.Verify_Web_Page import QaPlayground
from selenium.webdriver.common.by import By

def test_homepage_display(browser):
    qa_playground = QaPlayground(browser)

    # Given the qaplayground home page is displayed
    qa_playground.load()

    # And the browser title is 'Playground for the QA automation engineers'
    assert "Playground for the QA automation engineers" in browser.title
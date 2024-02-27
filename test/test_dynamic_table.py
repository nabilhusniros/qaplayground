"""
This module contain the dynamic table to find the spiderman in a table that changes the order
"""

from pages.Verify_Web_Page import QaPlayground
from selenium.webdriver.common.by import By

def  test_dynamic_table(browser):
    qa_playground = QaPlayground(browser)

# Given by the homepage is displayed
    qa_playground.load()

# When the user click dynamic table
    dynamic_table_link = browser.find_element(By.XPATH, '//main/div[3]/a[1]/div')
    dynamic_table_link.click()

# Then the user see the table 'Dynamic Table"
    assert "Test Dynamic Table" in browser.title

# And the user should find a row containing "Spiderman"
    spiderman_row = browser.find_element(By.XPATH, "//div[contains(@class, 'text-sm')][contains(., 'Spider-Man')]")
    assert 'Spider-Man' in spiderman_row.text

# And the user should be able to find his real name
    real_name = browser.find_element(By.XPATH, "//span[contains(@class, 'text-sm')][contains(., 'Peter Parker')]")
    assert "Peter Parker" in real_name.text

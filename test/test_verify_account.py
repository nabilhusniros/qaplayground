"""
This module contain the verify your account to enter a valid code
"""


from pages.Verify_Web_Page import QaPlayground
from selenium.webdriver.common.by import By

def test_verify_account(browser):
    qa_playground = QaPlayground(browser)

# Given by the homepage is displayed
    qa_playground.load()

# When the user click verify your account table
    verify_account = browser.find_element(By.XPATH, '//main/div[3]/a[2]')
    verify_account.click()

# Then the user input the correct confirmation code
    input_fields = browser.find_elements(By.XPATH, '//main/div/div/input')
    for field in input_fields:
        field.send_keys('9')
        assert field.get_attribute('value') == '9'

# And the user should see the success message
    result = browser.find_element(By.XPATH, '//main/div/small')
    assert "Success" in result.text
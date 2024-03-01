"""
This module contain the input box that need to add and remove the tags
"""


from pages.Verify_Web_Page import QaPlayground
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_input_tag(browser):
    qa_playground = QaPlayground(browser)

# Given by the homepage is displayed
    qa_playground.load()

# When the user click tags input box mini web page
    tag_page = browser.find_element(By.XPATH, '//main/div[3]/a[3]')
    tag_page.click()

# Then a new tag can be added with text
    tag_input = browser.find_element(By.CSS_SELECTOR, "input[type='text']")
    phrase = ['Python', 'Selenium', 'Pytest', 'Cool', 'Test', 'Automation', 'Hello', 'World']

    for word in phrase:
        tag_input.send_keys(word + Keys.RETURN)

# Then the user able to presence and count the tag
    added_tag = browser.find_elements(By.XPATH, f"//div/div/ul/li[text()='{word}']")
    for tag in added_tag:
        assert tag.is_displayed()

# And when the user try remove the tag
    browser.find_element(By.XPATH, '//div/button').click()
    current_count_element = browser.find_element(By.XPATH, "//div/div/p/span")

    assert current_count_element.text == "10"
    assert len(added_tag) == 0
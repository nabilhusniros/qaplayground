"""
This module contains shared fixtures
"""
import pytest
import selenium.webdriver
import json

@pytest.fixture
def config(scope='session'):

    #Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Retun config so it can be used
    return config

@pytest.fixture
def browser(config):
    
    # Initialize the ChromeDriver instance
    driver = selenium.webdriver.Chrome()

    # Make its calls wait up to 10 seconds
    driver.implicitly_wait(config['implicit_wait'])
    
    # Retrun the WebDriver instance for the setup
    yield driver

    # Delete all cookies before quitting the WebDriver instance
    driver.delete_all_cookies()

    # Quit the WebDriver instance for the cleanup
    driver.quit
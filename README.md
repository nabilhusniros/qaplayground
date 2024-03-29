# Project Title

QA Playground using pytest and selenium

## Description

This project showcases my practical test automation skills acquired through the QA Playground (https://qaplayground.dev/) exercise using Pytest and Selenium. It demonstrates finding and verifying elements to solidify automation concepts.

**Project Structure:**

* **pages:** This folder acts as a Python package and contains helper functions for interacting with specific QA Playground pages. For example, `qa_playground.py` provides methods to interact with the homepage elements.
* **test:** This folder contains pytest test cases. `conftest.py` holds shared fixtures like browser setup and test data, while individual test files like `dynamic_table.py` focus on automating specific exercises.

### Installing

1. Ensure Python and pip are installed (https://www.python.org/downloads/)
2. Install required dependencies:
```
pip install pytest
```
```
pip install selenium
```
4. Download the ChromeDriver version matching your browser and configure the path in your environment (https://chromedriver.chromium.org/).

**Note:** Adapt depending on your specific environment and requirements.

### Executing test

1. Clone or download this repository.
2. Run the pytest suite:
```
python -m pytest
```
4. To run a single file
```
python -m pytest test/home_page.py
```

## Authors
1. https://qaplayground.dev/ created by Marko Simic
2. Tester @nabilhusniros

## Potential Future Explorations
* Consider automating other QA Playground exercises to further refine my skills.
* Explore handling more complex scenarios like pagination, sorting, and filtering within the mini web apps
* Experiment with different locators and strategies for enhanced robustness.

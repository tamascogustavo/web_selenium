from locators.quote_locators import QuoteLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT_LOCATOR
        return self.parent.find_element(by=By.CSS_SELECTOR, value=locator).text

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR_LOCATOR
        return self.parent.find_element(by=By.CSS_SELECTOR, value=locator).text

    @property
    def tags(self):
        locator = QuoteLocators.TAGS_LOCATOR
        return [x.text for x in self.parent.find_elements(by=By.CSS_SELECTOR, value=locator)]

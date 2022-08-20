""""this search module"""
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class SearchPage:
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    URL = "https://www.amazon.eg/"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def search(self, phrase):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

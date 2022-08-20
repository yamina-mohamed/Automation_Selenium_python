from selenium.webdriver.common.by import By


class CartPage:

    DELETE_FROM_CART = (By.XPATH, "//input[@data-action='delete']")

    def __init__(self, driver):
        self.driver = driver

    def delete_item(self):
        self.driver.find_element(*self.DELETE_FROM_CART).click()

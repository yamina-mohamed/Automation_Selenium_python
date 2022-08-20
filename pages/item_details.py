from selenium.webdriver.common.by import By


class ItemDetailsPage:
    ADD_TO_CART = (By.ID, "add-to-cart-button")
    NAVIGATE_TO_CART = (By.XPATH, "//span[@id='sw-gtc']/descendant :: a")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART).click()

    def navigate_to_cart(self):
        self.driver.find_element(*self.NAVIGATE_TO_CART).click()

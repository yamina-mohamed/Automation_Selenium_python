from selenium.webdriver.common.by import By


class ResultPage:
    # RESULT_LINK = (By.CSS_SELECTOR, 'a.result a')
    # SEARCH_INPUT = (By.ID, 'search_form_input')
    CHECK_BOX = (By.XPATH, '//li[@id="p_89/OPPO"]/descendant :: i')
    # MORE_BTN = (By.XPATH, '//div[@data-component-type="s-search-result"]')
    #  CHECK_BOX = (By.XPATH, '//li[@id="p_89/HTC"]/descendant :: i')
    RESULT_LIST = (By.XPATH, '//div[@data-component-type="s-search-result"]')

    def __init__(self, driver):
        self.driver = driver

    def result_link_title(self):
        links = self.driver.find_elements(*self.RESULT_LINK)
        titles = [link.text for link in links]
        return titles

    def click_on_checkbox(self):
        self.driver.find_element(*self.CHECK_BOX).click()

    def title(self):
        links = self.driver.find_elements(*self.RESULT_LIST)
        element = links[-1]
        element.click()

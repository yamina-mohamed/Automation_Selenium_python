import pytest
import selenium.webdriver


@pytest.fixture
def browser():
    # inisialize chrome driver instance
    driver = selenium.webdriver.Chrome()
    # makes it's call to wait 10 seconds to make elements appears
    driver.implicitly_wait(10)
    # return the webdriver for setup
    yield driver
    # quit the webdriver for the clean up
    driver.quit()




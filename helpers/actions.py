from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class ActionHelper:
    def __init__(self, driver):
        self.driver = driver
        self._actions = ActionChains(driver)

    def click(self, element):
        """Move to element and click using ActionChains."""
        self._actions.move_to_element(element).click().perform()

    def page_down(self):
        """Send a page down keypress."""
        self._actions.send_keys(Keys.PAGE_DOWN).perform()

    def move_to(self, element):
        """Move to element without clicking."""
        self._actions.move_to_element(element).perform()

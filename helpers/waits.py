from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Waits:
    def __init__(self, driver):
        self.driver = driver

    def set_implicit(self, seconds: int):
        """Set implicit wait on the driver."""
        self.driver.implicitly_wait(seconds)

    def explicit_visibility(self, by, locator, timeout: int = 15):
        """Wait until element is visible and return it."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, locator))
        )

    def fluent_find(self, by, locator, timeout: int = 20, poll_frequency: int = 2, ignored_exceptions=None):
        """Fluent-style wait (returns element when found)."""
        return WebDriverWait(
            self.driver,
            timeout=timeout,
            poll_frequency=poll_frequency,
            ignored_exceptions=ignored_exceptions,
        ).until(lambda d: d.find_element(by, locator))

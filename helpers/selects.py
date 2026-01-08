from selenium.webdriver.support.ui import Select


class SelectHelper:
    def __init__(self, driver):
        self.driver = driver

    def select_by_visible_text(self, select_element, text: str):
        Select(select_element).select_by_visible_text(text)

    def select_by_value(self, select_element, value: str):
        Select(select_element).select_by_value(value)

    def select_by_index(self, select_element, index: int):
        Select(select_element).select_by_index(index)

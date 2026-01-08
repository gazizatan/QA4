from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

from helpers import Waits, ActionHelper, SelectHelper


def test_advanced_selenium(driver):
    waits = Waits(driver)
    actions = ActionHelper(driver)
    selects = SelectHelper(driver)

    waits.set_implicit(10)

    driver.get("https://demoqa.com/automation-practice-form")

    first_name = waits.explicit_visibility(By.ID, "firstName", timeout=15)
    first_name.send_keys("Gaziza")

    driver.find_element(By.ID, "lastName").send_keys("Tanirbergen")
    driver.find_element(By.ID, "userEmail").send_keys("test@email.com")
    driver.find_element(By.ID, "userNumber").send_keys("1234567890")
    driver.find_element(By.ID, "currentAddress").send_keys("123 Test St, Test City")

    gender = driver.find_element(By.XPATH, "//label[text()='Female']")
    actions.click(gender)
    actions.page_down()

    driver.find_element(By.ID, "dateOfBirthInput").click()

    month_el = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    year_el = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")

    selects.select_by_visible_text(month_el, "May")
    selects.select_by_visible_text(year_el, "2004")

    driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day--022')]").click()

    submit_button = waits.fluent_find(By.ID, "submit", timeout=20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])

    driver.execute_script("arguments[0].click();", submit_button)

    modal_title = waits.explicit_visibility(By.ID, "example-modal-sizes-title-lg", timeout=15)
    assert modal_title.text == "Thanks for submitting the form"

    time.sleep(2)

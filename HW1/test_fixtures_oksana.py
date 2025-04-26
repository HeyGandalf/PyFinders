import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    def _login(username, password):
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.CLASS_NAME, "btn").click()
    return _login

def test_positive_login(driver, login):
    login("student", "Password123")
    time.sleep(2)
    current_url = driver.current_url
    expected_text = driver.find_element(By.CLASS_NAME, "post-title").text
    logout_button = driver.find_element(By.CLASS_NAME, "wp-block-button__link")
    assert current_url == "https://practicetestautomation.com/logged-in-successfully/", f"Expected url 'https://practicetestautomation.com/logged-in-successfully/', but got '{current_url}"
    assert  expected_text == "Logged In Successfully", "wrong text"
    assert logout_button.is_displayed(), "Button 'Log out' is not displayed"

def test_negative_username(driver, login):
    login("incorrectUser", "Password123")
    time.sleep(2)
    error = driver.find_element(By.CLASS_NAME, "show")
    expected_text = driver.find_element(By.CLASS_NAME, "show").text
    assert error.is_displayed(), "Username error message is not displayed"
    assert expected_text == "Your username is invalid!", f"Expected error message: 'Your username is invalid!', but displayed {expected_text}"

def test_negative_password(driver, login):
    login("student", "incorrectPassword")
    time.sleep(2)
    error = driver.find_element(By.CLASS_NAME, "show")
    expected_text = driver.find_element(By.CLASS_NAME, "show").text
    assert error.is_displayed(), "Password error message is not displayed"
    assert expected_text == "Your password is invalid!", f"Expected error message: 'Your password is invalid!', but displayed {expected_text}"
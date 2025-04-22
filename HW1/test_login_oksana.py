from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.CLASS_NAME, "btn").click()

    time.sleep(2)

    assert driver.current_url == "https://practicetestautomation.com/logged-in-successfully/"
    assert driver.find_element(By.CLASS_NAME, "post-title").text == "Logged In Successfully"
    button = driver.find_element(By.CLASS_NAME, "wp-block-button__link")
    assert button.is_displayed()




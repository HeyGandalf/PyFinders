from selenium import webdriver
from selenium.webdriver.common.by import (By)

def test_error_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, value='user-name').send_keys("error_user")
    driver.find_element(By.ID, value='password').send_keys("secret_sauce")
    driver.find_element(By.NAME, value='login-button').click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    driver.quit()


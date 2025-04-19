import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_login_saucedemo(driver):
    """Проверка успешного логина на сайте saucedemo.com"""
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    username_field = driver.find_element(By.ID, "user-name")
    username_field.clear()
    username_field.send_keys("standard_user")
    assert username_field.get_attribute("value") == "standard_user", "Поле 'Username' заполнено некорректно"

    password_field = driver.find_element(By.CSS_SELECTOR, '[data-test="password"]')
    password_field.clear()
    password_field.send_keys("secret_sauce")
    assert password_field.get_attribute("value") == "secret_sauce", "Поле 'Password' заполнено некорректно"

    login_button = driver.find_element(By.CSS_SELECTOR, ".submit-button.btn_action")
    login_button.click()

    inventory_container = wait.until(EC.presence_of_element_located((By.ID, "inventory_container")))
    assert inventory_container.is_displayed(), "Не удалось авторизоваться на сайте"

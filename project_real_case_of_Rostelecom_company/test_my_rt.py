import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://my.rt.ru/"


def test_page_loads(driver):
    """
   1.Тест проверяет загрузку страницы и наличие "Ростелеком" в заголовке.
    """
    driver.get(URL)
    # Явное ожидание загрузки заголовка страницы
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains("Ростелеком"))
    # Вывод заголовка для отладки
    print(driver.title)
    assert "Ростелеком" in driver.title


def test_login_form_is_displayed(driver):
    """
   2.Тест проверяет, что форма входа отображается на странице.
    """
    driver.get(URL)
    login_form = driver.find_element(By.ID, "page-right")
    assert login_form.is_displayed()


def test_login_button_is_clickable(driver):
    """
    3.Тест проверяет, что кнопка входа доступна для нажатия.
    """
    driver.get(URL)
    login_button = driver.find_element(By.XPATH, "//button[@type='submit' and @name='login']")
    assert login_button.is_enabled()


def test_login_with_empty_credentials(driver):
    """
    4.Тест проверяет, что при попытке входа с пустыми полями отображается сообщение об ошибке.
    """
    driver.get(URL)
    login_button = driver.find_element(By.XPATH, "//button[@type='submit' and @name='login']")
    login_button.click()
    error_message = driver.find_element(By.ID, "username-meta")
    assert error_message.is_displayed()

def test_explicit_wait_for_login_button(driver):
    """
    5.Тест использует явное ожидание для проверки отображения кнопки входа.
    """
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and @name='login']")))
    assert login_button.is_displayed()


def test_login_with_invalid_credentials(driver):
    """
    6.Тест проверяет, что при попытке входа с неверными учетными данными отображается сообщение об ошибке.
    """
    driver.get(URL)
    find_login = driver.find_element(By.ID, "t-btn-tab-login")
    find_login.click()

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_input.send_keys("invalid_user")
    password_input.send_keys("invalid_pass")
    login_button.click()

    error_message = driver.find_element(By.ID, "form-error-message")
    assert error_message.is_displayed()

def test_reset_password_link(driver):
    """
    7.Тест проверяет, что ссылка для восстановления пароля отображается на странице.
    """
    driver.get(URL)
    reset_password_link = driver.find_element(By.LINK_TEXT, "Забыл пароль")
    assert reset_password_link.is_displayed()



def test_login_form_placeholder_text(driver):
    """
    8.Тест проверяет, что поля ввода логина и пароля содержат правильные текстовые подсказки (placeholder).
    """
    driver.get(URL)
    username_placeholder = driver.find_element(By.XPATH, "//input[@id='username']/following-sibling::span[@class='rt-input__placeholder']")
    assert username_placeholder.is_displayed()
    assert username_placeholder.text == "Мобильный телефон"
    password_placeholder = driver.find_element(By.XPATH, "//input[@id='password']/following-sibling::span[@class='rt-input__placeholder']")
    assert password_placeholder.is_displayed()
    assert password_placeholder.text == "Пароль"


def test_successful_login(driver):
    """
    9.Тест проверяет успешный вход в систему с валидными учетными данными.
    """
    driver.get(URL)
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # указать валидные username и пароль
    username_input.send_keys("valid_user")
    password_input.send_keys("valid_pass")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.url_changes(URL))
    assert "dashboard" in driver.current_url


def test_navigation_to_support_page(driver):
    """
    10.Тест проверяет навигацию к странице помощи.
    """
    driver.get(URL)
    support_link = driver.find_element(By.LINK_TEXT, "Помощь")
    support_link.click()
    assert support_link.is_displayed()



def test_forgot_password_functionality(driver):
    """
    11.Тест проверяет функцию восстановления пароля.
    """
    driver.get(URL)
    forgot_password_link = driver.find_element(By.LINK_TEXT, "Забыл пароль")
    forgot_password_link.click()
    WebDriverWait(driver, 10).until(EC.url_contains("reset-credentials"))
    assert "reset-credentials" in driver.current_url





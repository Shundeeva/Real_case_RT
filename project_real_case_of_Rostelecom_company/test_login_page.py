import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://lk.rt.ru/"


def test_page_loads(driver):
    """
    1.Тест проверяет загрузку страницы и наличие "Ростелеком" в заголовке.
    """
    driver.get(URL)
    assert "Ростелеком" in driver.title


def test_login_form_is_displayed(driver):
    """
    2.Тест проверяет, что форма входа отображается на странице.
    """
    driver.get(URL)
    login_form = driver.find_element(By.ID, "page-right")
    assert login_form.is_displayed()


def test_code_button_is_clickable(driver):
    """
   3.Тест проверяет, что кнопка "Получить код" доступна для нажатия.
    """
    driver.get(URL)
    login_button = driver.find_element(By.ID, "otp_get_code")
    assert login_button.is_enabled()


def test_login_button_is_clickable(driver):
    """
   4.Тест проверяет, что кнопка "Войти с паролем" доступна доступна для нажатия.
    """
    driver.get(URL)
    login_button = driver.find_element(By.ID, "standard_auth_btn")
    assert login_button.is_enabled()


def test_login_with_empty_credentials(driver):
    """
    5.Тест проверяет, что при попытке входа с пустыми полями отображается сообщение об ошибке.
    """
    driver.get(URL)
    login_button = driver.find_element(By.ID, "otp_get_code")
    login_button.click()
    error_message = driver.find_element(By.ID, "address-meta")
    assert error_message.is_displayed()



def test_explicit_wait_for_login_button(driver):
    """
    6.Тест использует явное ожидание для проверки отображения кнопки входа.
    """
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    assert login_button.is_displayed()


def test_login_with_invalid_credentials(driver):
    """
    7.Тест проверяет, что при попытке входа с неверными учетными данными отображается сообщение об ошибке.
    """
    driver.get(URL)
    standart_button = driver.find_element(By.ID, "standard_auth_btn")
    standart_button.click()
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
    8.Тест проверяет, что ссылка для восстановления пароля отображается на странице.
    """
    driver.get(URL)
    standart_button = driver.find_element(By.ID, "standard_auth_btn")
    standart_button.click()
    find_login = driver.find_element(By.ID, "t-btn-tab-login")
    find_login.click()
    reset_password_link = driver.find_element(By.LINK_TEXT, "Забыл пароль")
    assert reset_password_link.is_displayed()


def test_explicit_wait_for_username_field(driver):
    """
    9.Тест использует явное ожидание для проверки отображения поля ввода логина.
    """
    driver.get(URL)
    standart_button = driver.find_element(By.ID, "standard_auth_btn")
    standart_button.click()
    find_login = driver.find_element(By.ID, "t-btn-tab-login")
    find_login.click()
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    assert username_input.is_displayed()


def test_login_form_placeholder_text(driver):
    """
    10.Тест проверяет, что поля ввода логина и пароля содержат правильные текстовые подсказки (placeholder).
    """
    driver.get(URL)
    standart_button = driver.find_element(By.ID, "standard_auth_btn")
    standart_button.click()
    find_login = driver.find_element(By.ID, "t-btn-tab-mail")
    find_login.click()
    username_placeholder = driver.find_element(By.XPATH, "//input[@id='username']/following-sibling::span[@class='rt-input__placeholder']")
    assert username_placeholder.is_displayed()
    assert username_placeholder.text == "Электронная почта"
    password_placeholder = driver.find_element(By.XPATH, "//input[@id='password']/following-sibling::span[@class='rt-input__placeholder']")
    assert password_placeholder.is_displayed()
    assert password_placeholder.text == "Пароль"



def test_successful_login(driver):
    """
    11. Тест проверяет успешный вход в систему с валидными учетными данными, используя адрес почты.
    """
    driver.get(URL)
    standart_button = driver.find_element(By.ID, "standard_auth_btn")
    standart_button.click()
    find_login = driver.find_element(By.ID, "t-btn-tab-mail")
    find_login.click()
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Указать валидные почту и пароль
    username_input.send_keys("valid_user")
    password_input.send_keys("valid_pass")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.url_changes(URL))
    assert "dashboard" in driver.current_url


def test_logout_functionality(driver):
    """
    12. Тест проверяет функцию выхода из системы.
    """
    driver.get(URL)
    standart_button = driver.find_element(By.ID, "standard_auth_btn")
    standart_button.click()
    find_login = driver.find_element(By.ID, "t-btn-tab-mail")
    find_login.click()
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # указать валидные username и пароль
    username_input.send_keys("username")
    password_input.send_keys("password")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.url_changes(URL))

    # logout
    logout_window = driver.find_element(By.XPATH, "// *[ @ id = 'root'] / div / div / div[1] / div / div[1] / div[3] / div[2] / h2")
    logout_window.click()

    logout_button = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[3]/button")
    logout_button.click()

    # Verify logout
    assert "login" in driver.current_url




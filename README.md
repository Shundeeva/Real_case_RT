# Тестирование веб-приложения Ростелеком

Этот проект содержит тесты для проверки функциональности веб-приложения Ростелеком. Тесты написаны с использованием фреймворка `pytest` и `selenium` для автоматизированного тестирования веб-интерфейсов.

## Структура проекта

Проект включает следующие файлы:
- `conftest.py`: содержит фикстуры для настройки и завершения работы веб-драйвера.
- `test_login_page.py`: содержит тесты для проверки функциональности страницы входа по URL `https://lk.rt.ru/`.
- `test_my_rt.py`: содержит тесты для проверки функциональности основной страницы по URL `https://my.rt.ru/`.

## Описание тестовых сценариев

### test_login_page.py

1. **test_page_loads**
    - **Описание**: Проверяет загрузку страницы и наличие "Ростелеком" в заголовке.
2. **test_login_form_is_displayed**
    - **Описание**: Проверяет, что форма входа отображается на странице.
3. **test_code_button_is_clickable**
    - **Описание**: Проверяет, что кнопка "Получить код" доступна для нажатия.
4. **test_login_button_is_clickable**
    - **Описание**: Проверяет, что кнопка "Войти с паролем" доступна для нажатия.
5. **test_login_with_empty_credentials**
    - **Описание**: Проверяет, что при попытке входа с пустыми полями отображается сообщение об ошибке.
6. **test_explicit_wait_for_login_button**
    - **Описание**: Использует явное ожидание для проверки отображения кнопки входа.
7. **test_login_with_invalid_credentials**
    - **Описание**: Проверяет, что при попытке входа с неверными учетными данными отображается сообщение об ошибке.
8. **test_reset_password_link**
    - **Описание**: Проверяет, что ссылка для восстановления пароля отображается на странице.
9. **test_explicit_wait_for_username_field**
    - **Описание**: Использует явное ожидание для проверки отображения поля ввода логина.
10. **test_login_form_placeholder_text**
    - **Описание**: Проверяет, что поля ввода логина и пароля содержат правильные текстовые подсказки (placeholder).
11. **test_successful_login**
    - **Описание**: Проверяет успешный вход в систему с валидными учетными данными.
12. **test_logout_functionality**
    - **Описание**: Проверяет функцию выхода из системы.

### test_my_rt.py

1. **test_page_loads**
    - **Описание**: Проверяет загрузку страницы и наличие "Ростелеком" в заголовке.
2. **test_login_form_is_displayed**
    - **Описание**: Проверяет, что форма входа отображается на странице.
3. **test_login_button_is_clickable**
    - **Описание**: Проверяет, что кнопка входа доступна для нажатия.
4. **test_login_with_empty_credentials**
    - **Описание**: Проверяет, что при попытке входа с пустыми полями отображается сообщение об ошибке.
5. **test_explicit_wait_for_login_button**
    - **Описание**: Использует явное ожидание для проверки отображения кнопки входа.
6. **test_login_with_invalid_credentials**
    - **Описание**: Проверяет, что при попытке входа с неверными учетными данными отображается сообщение об ошибке.
7. **test_reset_password_link**
    - **Описание**: Проверяет, что ссылка для восстановления пароля отображается на странице.
8. **test_login_form_placeholder_text**
    - **Описание**: Проверяет, что поля ввода логина и пароля содержат правильные текстовые подсказки (placeholder).
9. **test_successful_login**
    - **Описание**: Проверяет успешный вход в систему с валидными учетными данными.
10. **test_navigation_to_support_page**
    - **Описание**: Проверяет навигацию к странице помощи.
11. **test_forgot_password_functionality**
    - **Описание**: Проверяет функцию восстановления пароля.

   ## Для запуска всех тестов используйте команду:
pytest

   ## Если необходимо запустить тесты из конкретного файла, используйте команду:
pytest test_login_page.py

_или_

pytest test_my_rt.py

   ## Для получения подробного отчета о выполнении тестов используйте флаг -v:
pytest -v

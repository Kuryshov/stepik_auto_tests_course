import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
# pytest -s -v -m "smoke or regression" test_fixture8.py
link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    # Запуск через терминал pytest -s -v -m "smoke or regression" test_fixture8.py
    # Флаги для запуска. -s выводить в консоль принты, -v выводить полный отчёт, -m запускать маркированные тесты.
    @pytest.mark.smoke  # mark.smoke маркировка критичного теста
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression  # mark.regression маркировка регрессионного теста, запуск перед релизом
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

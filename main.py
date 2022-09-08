# pip install selenium
# chromedriver.exe драйвер для открытия нового окна хрома

import time
import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/find_link_text'
# Инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
try:
    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
    browser.get(link)

    link_1 = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000)))
    link_1.click()
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')  # вместо пробела писать точку в value
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # button = browser.find_element(by='xpath', value="/html/body/div/form//div//button[@type='submit']")
    # button.click()

finally:
    # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

import time
import math
import pytest

from selenium.webdriver.common.by import By


def count():
    answer = math.log(int(time.time()))
    return answer


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
def test_parametrize(browser, link):
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'textarea').send_keys(count())
    browser.find_element(By.CSS_SELECTOR, 'button.submit-submission[type="button"]').click()
    correct_text = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    assert 'Correct!' == correct_text
    # try:
    #     assert 'Correct!' == correct_text
    # except AssertionError:
    #     correct_text(correct_text)

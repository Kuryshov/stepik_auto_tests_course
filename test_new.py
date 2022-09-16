import unittest

from selenium import webdriver


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        try:
            browser.get(link)
            browser.find_element(by='css selector', value='input.form-control.first:required').send_keys("Ivan")
            browser.find_element(by='css selector', value='input.form-control.second:required').send_keys("Petrov")
            browser.find_element(by='css selector', value='input.form-control.third:required').send_keys("Smolensk")
            browser.find_element(by='css selector', value='button.btn').click()

            welcome_text_elt = browser.find_element(by='tag name', value='h1')
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'sda')

        finally:
            browser.quit()

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        try:

            browser.get(link)
            browser.find_element(by='css selector', value='input.form-control.first:required').send_keys("Ivan")
            browser.find_element(by='css selector', value='input.form-control.second:required').send_keys("Petrov")
            browser.find_element(by='css selector', value='input.form-control.third:required').send_keys("Smolensk")
            browser.find_element(by='css selector', value='button.btn').click()

            welcome_text_elt = browser.find_element(by='tag name', value='h1')
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Косяк')

        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()

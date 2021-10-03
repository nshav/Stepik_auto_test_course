from selenium import webdriver
import time
import unittest

browser = webdriver.Chrome()

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Nikita")
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("Shavandin")
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("SPb")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registeration is failed")
        
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Nikita")
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("Shavandin")
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("SPb")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registeration is failed")
        
if __name__ == "__main__":
    unittest.main()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()

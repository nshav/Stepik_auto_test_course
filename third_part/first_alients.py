from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import pytest
import time


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class Test_help_me():
	@pytest.mark.parametrize('site', ["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1","https://stepik.org/lesson/236898/step/1","https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1","https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])
	def test_guest_input(self,browser, site):
		link = f"{site}"
		browser.get(link)
		time.sleep(5)
		#browser.implicitly_wait(10)
		answer = math.log(int(time.time()))
		
		input1 = browser.find_element_by_css_selector('.quiz-component textarea')
		input1.send_keys(str(answer))
		
		button = WebDriverWait(browser, 5).until(
		    EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
		)
		button.click()
		time.sleep(5)	
		message = WebDriverWait(browser, 5).until(
			EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
		).text
		text_1 = ""
		if (message != "Correct!"):
			text_1 += massage
		print(text_1)

if __name__ == "__main__":
    unittest.main()
    #The owls are not what they seem! OvO
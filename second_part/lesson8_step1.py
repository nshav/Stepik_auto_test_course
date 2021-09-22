from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("alert('Robots at work');")

    #def calc(x):
    #    return str(math.log(abs(12*math.sin(int(x)))))

    x1_element = browser.find_element_by_id("num1")
    x2_element = browser.find_element_by_id("num2")
    x1 = int(x1_element.text)
    x2 = int(x2_element.text)
    #y = x1 + x2
    #y = calc(x)

    # Ваш код, который заполняет обязательные поля
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(x1 + x2))

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn-default")
    button.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
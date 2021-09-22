from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #первая страница
    button = browser.find_element_by_tag_name("button")
    button.click()
    confirm = browser.switch_to.alert
    time.sleep(3)
    confirm.dismiss()
    button.click()
    confirm = browser.switch_to.alert
    time.sleep(3)
    confirm.accept()

    #вторая страница

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)  

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
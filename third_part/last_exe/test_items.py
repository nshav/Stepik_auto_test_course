import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    time.sleep(15)
    browser.find_element_by_css_selector("#add_to_basket_form button")
    assert is_element_present(browser)==True, "button is't defined"
import time
from selenium.webdriver.common.by import By


def test_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    btn_add = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert btn_add, "No 'Add to basket' button on the page"

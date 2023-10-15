import time
from selenium.webdriver.common.by import By


def test_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")) > 0, "No 'Add to basket' button on the page"

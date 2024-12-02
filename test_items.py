import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_add_to_cart_button_exists(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)  # Задержка для визуальной проверки языка
    # Ищем кнопку добавления в корзину
    add_to_cart_button = browser.find_element("css selector", ".btn-add-to-basket")
    # Проверяем, что кнопка присутствует
    assert add_to_cart_button.is_displayed(), "Add to cart button is not displayed!"
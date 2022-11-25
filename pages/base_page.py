from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
link = "http://selenium1py.pythonanywhere.com/"
browser = webdriver.Chrome()
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def open(self):
        self.browser.get(self.url)

page = BasePage(browser, link)
# открываем нужную страницу
page.open()
from selenium.webdriver.common.by import By
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"
browser = webdriver.Chrome()
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

page = BasePage(browser, link)
# открываем нужную страницу
page.open()
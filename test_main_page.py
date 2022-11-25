from selenium.webdriver.common.by import By

from course_step_git.pages.base_page import page
from pages.main_page import MainPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

#def go_to_login_page(browser):
#    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#    login_link.click()

#def test_guest_can_go_to_login_page(browser):
#   link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#    page.open()                      # открываем страницу
#   page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

#def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)
#    page.open()
#    page.should_be_login_link()
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    login_page = LoginPage(browser, link)
	# открываем нужную страницу
    page.open()
	# выполняем метод страницы: переходим на страницу логина
    page.go_to_login_page()
    login_page.should_be_login_page()
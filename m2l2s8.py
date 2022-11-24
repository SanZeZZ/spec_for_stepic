from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math
import os



link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

element1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
element1.send_keys('Name')
element2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
element2.send_keys('LastName')
element3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
element3.send_keys('e@mai.l')
element4 = browser.find_element(By.ID, "file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')
element4.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button.click()

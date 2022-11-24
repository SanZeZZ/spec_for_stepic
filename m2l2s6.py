from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(int(x))

button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
browser.execute_script('window.scrollBy(0, 100);')

element1 = browser.find_element(By.ID, 'answer')
element1.send_keys(y)

option1 = browser.find_element(By.ID, 'robotCheckbox')
option1.click()
option2 = browser.find_element(By.ID, "robotsRule")
option2.click()
button.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, pyperclip


opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)

# переходим на нужную страницу
browser = webdriver.Chrome(options=opt)
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

# находим цену дома и ждем, пока она не станет 10 000 RUR, бронируем
button = browser.find_element_by_id("book")
price = WebDriverWait(browser, 15).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
)
button.click()

# находим значение x для выполнения задания
x_string = browser.find_element(By.ID, "input_value")
x_number = int( x_string.text )

# высчитываем результат для задания
answer = calc(x_number)

# вводим результат в поле ввода
input_answer = browser.find_element(By.ID, "answer")
input_answer.send_keys(answer)

# нажимаем на кнопку
send_button = browser.find_element(By.ID, "solve")
send_button.click()

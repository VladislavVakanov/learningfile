import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

from selenium.webdriver.support.wait import WebDriverWait

def func(x):
    return str(math.log(abs(12 * math.sin(x))))



browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)

but = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
but.click()
input1 = browser.find_elements(By.CLASS_NAME,"input_value")
input = browser.find_element(By.ID,"input_value")

inp = browser.find_element(By.ID, "answer")
inp.send_keys(func(int(input.text)))

but = browser.find_element(By.ID, "solve")
but.click()
time.sleep(6)



import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
import json

driver = webdriver.Chrome()

url = "https://justpaste.it/"

file = open('aaa.html')
data = file.read()
driver.get(url)
time.sleep(5)
driver.find_element(by=By.XPATH, value="//input[@placeholder='Title']").send_keys("nfjdshbfjhdbshj")

text_area = driver.find_element(by=By.TAG_NAME, value="iframe").send_keys(data)
# text_area = driver.find_element(by=By.CLASS_NAME, value="tox-edit-area")
# text_area.click()
# driver.execute_script("arguments[0].textContent = arguments[1];", text_area, "This is a test")

driver.find_element(by=By.CLASS_NAME, value="publishButton").click()
time.sleep(2)
captcha = driver.find_element(by=By.CLASS_NAME, value="captchaGridContainer").get_attribute('outerHTML')
correct_word = driver.find_element(by=By.CLASS_NAME, value="correctWord").text
print(captcha)
print("-------------------")
print(correct_word)
time.sleep(5)
print(driver.current_url)
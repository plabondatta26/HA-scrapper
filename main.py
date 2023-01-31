import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
import json

driver = webdriver.Chrome()

url = "https://justpaste.it/"

driver.get(url)
time.sleep(5)
driver.find_element(by=By.XPATH, value="//input[@placeholder='Title']").send_keys("nfjdshbfjhdbshj")

text_area = driver.find_element(by=By.CLASS_NAME, value="tox-edit-area")
text_area.click()
driver.execute_script("arguments[0].textContent = arguments[1];", text_area, "This is a test")

driver.find_element(by=By.CLASS_NAME, value="publishButton").click()
time.sleep(5)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from credentials import username, password
import time
import random


def login(username, password):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/usr/bin/chromium-gost"
    browser = webdriver.Chrome(chrome_options=chrome_options)

    try:
        browser.get('https://ngate:444')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element(By.NAME, 'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element(By.NAME,'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

        browser.close()
        browser.quit()
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


login(username, password)


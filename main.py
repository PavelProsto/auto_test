from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import username, password, url, publish_config
import time
import random



def login_ldap(username, password, url, first_config):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/usr/bin/chromium-gost"
    browser = webdriver.Chrome(chrome_options=chrome_options)

    try:
        browser.get(url)
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
        browser.get(publish_config)
       #time.sleep(random.randrange(3, 5))
       #button_path = '/html/body/div/div[1]/section[1]/h1/form[2]/button'
       #browser.get(first_config)
       #WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, button_path))).click()
        time.sleep(30)
        #publish_config = browser.find_element(By.XPATH, "/html/body/form[1]")
#        browser.close()
#        browser.quit()
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


#def go_to_active_config(url):
#    chrome_options = webdriver.ChromeOptions()
#    chrome_options.binary_location = "/usr/bin/chromium-gost"
#    browser = webdriver.Chrome(chrome_options=chrome_options)

#    try:
#        browser.get(url+'serverconfig/site/index/1/')
#        time.sleep(random.randrange(3, 5))
#        active_config = browser.find_element(By.XPATH, "/html/body/div/div[1]/section[1]/h1/form[2]/button")


#    except Exception as ex:
#        print(ex)
#        browser.close()
#        browser.quit()


login_ldap(username, password, url, publish_config)
#go_to_active_config(url)


#/html/body/div/aside/section/ul/li[3]/ul/li[2]/a

#http://192.168.10.99:8000/serverconfig/site/index/1/

#/html/body/div/div[1]/section[1]/h1/form[2]/button

#/html/body/div/div[1]/section[1]/h1/form[2]/button

#http://192.168.10.99:8000/serverconfig/configuration/publish/4/
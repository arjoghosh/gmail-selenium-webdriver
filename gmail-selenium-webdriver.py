# Author : Arjo Ghosh আর্য্য ঘোষ

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
x=input("Enter username :\t")
x=x.strip()
y=input("Enter password :\t")
browser = webdriver.Firefox()
browser.get('http://gmail.com')
action = webdriver.ActionChains(browser)
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys(x)
nextButton = browser.find_element_by_id('next')
nextButton.click()
time.sleep(1)
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys(y)
signinButton = browser.find_element_by_id('signIn')
signinButton.click()

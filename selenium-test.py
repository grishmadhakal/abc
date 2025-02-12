from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()

browser.get('https://yahoo.com')
time.sleep(2)

searchBar = browser.find_element(By.ID, 'ybar-sbq')
searchBar.send_keys('grishma')
searchBar.submit()
time.sleep(5)

browser.quit()
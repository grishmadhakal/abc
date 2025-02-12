from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()

browser.get('https://bing.com')
time.sleep(2)

searchBar = browser.find_element(By.ID, 'sb_form_q')
searchBar.send_keys('Quantum Infosys Pvt. Ltd')
searchBar.submit()
time.sleep(5)

browser.quit()
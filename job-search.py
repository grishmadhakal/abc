from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()

jobList = ["QA", "PHP", "Java", "Python"]

for job in jobList:
    print(job)
    browser.get('https://merojob.com')
    searchBar = browser.find_element(By.ID, 'job_search')
    searchBar.send_keys(job)
    searchBar.submit()

    # Find all <a> elements with href attributes
    links = browser.find_elements(By.TAG_NAME, 'h1')

    # Loop through each link and print the title attribute
    for link in links:
        print(link.text)

    time.sleep(3)

time.sleep(5)
browser.quit()
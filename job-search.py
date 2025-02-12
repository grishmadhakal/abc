from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument("--headless=new")

browser = webdriver.Edge(options = options)


jobList = ["QA", "PHP", "Java", "Python"]
my_String =""

for job in jobList:
    print(job)
    browser.get('https://merojob.com')
    searchBar = browser.find_element(By.ID, 'job_search')
    searchBar.send_keys(job)
    searchBar.submit()

    # Find all <a> elements with href attributes
    links = browser.find_elements(By.TAG_NAME, 'h1')

    # Loop through each link and print the title attribute
    my_String +=f"jobs for {job}:\n"
    for link in links:
        print(link.text)
        my_String += link.text + "\n"
        my_String += "\n"
        time.sleep(3)
        print(my_String)
        file = open('test.txt','w')
        file.write(my_String)

file.close()

time.sleep(5)
browser.quit()
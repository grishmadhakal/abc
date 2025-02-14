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
    print(f"Searching for jobs: {job}")
    browser.get('https://merojob.com')
    searchBar = browser.find_element(By.ID, 'job_search')
    searchBar.send_keys(job)
    searchBar.submit()

    time.sleep(2)  # Allow time for the page to load

    # Find all relevant elements containing job titles (update selector as needed)
    links = browser.find_elements(By.TAG_NAME, 'h1')

    # Add job titles under the corresponding job category in a structured format
    my_string += f"Jobs for {job}:\n"
    for link in links:
        print(link.text)
        my_string += f"- {link.text}\n"
    my_string += "\n"  # Add a blank line after each category

time.sleep(3)
print(my_string)
file = open('test.txt', 'w', encoding='utf-8')
file.write(my_string)
file.close()

time.sleep(5)
browser.quit()
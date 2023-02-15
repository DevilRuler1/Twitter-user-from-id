from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get('https://tweeterid.com/')
file1 = open('ID.txt', 'r')
Lines = file1.readlines()
ids = []

for line in Lines:
    ids.append(line.strip())

users = []
for i in ids:
    driver.find_element_by_id("twitter").send_keys(i)
    driver.find_element_by_id("twitter").submit()
    time.sleep(2)
    out = driver.find_element_by_id("0")
    out = out.text.split("=>")[1].strip()
    print(i + " = " + out)
    users.append(out)
    driver.refresh()

driver.close()

output = {"id":ids, "user":users}
new = pd.DataFrame.from_dict(output)
new = new.set_index('id')
new.to_csv("users.csv")
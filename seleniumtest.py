testsite_array = []
with open('test5.csv') as my_file:
    for line in my_file:
        testsite_array.append(line)

for x in range(len(testsite_array)): 
    print(testsite_array[x]) 

"""
import re

s = 'asdf=5;iwantthis123jasd'
result = re.search('asdf=5;(.*)123jasd', s)
link = "https://www.instagram.com/clayvalentinex/"
res = re.search('https://www.instagram.com/(.*)/', link)
print(result.group(1))
print(res.group(2))
"""



"""
from selenium import webdriver
import time

driver =webdriver.Chrome()

url = "http://github.com"

driver.get(url)

time.sleep(2)
driver.maximize_window()
print(driver.title)

time.sleep(2)
driver.close()

"""
"""
Selenium open webbrowser

from selenium import webdriver

driver = webdriver.Chrome()

url = "http://google.com"

driver.get(url)
"""
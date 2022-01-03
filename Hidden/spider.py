from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pandas as pd

#setup
binary = FirefoxBinary("*FIREFOX BINARY*")
driver = webdriver.Firefox(firefox_binary = binary)
url = '' #starting point for spider
driver.get(url)

#anti-crawling workarounds
#bypass captcha
driver.implicitly_wait(10000)
#NOTE: if server identifies spider as a bot, scraping will have to be done 
# in smaller chunks and then combined into a master csv using combine.py

#find elements
driver.find_element_by_class_name("") #use the html element name
driver.find_element_by_xpath('') #alternatively, use xpath name
driver.find_elements_by_class_name("").text #find multiple elements and retrieve their text

#store elements
content = []
text = driver.find_element_by_class_name('').text
content.append(text)

#handle multiple pages
for i in range(1, 10): #replace 10 with number of pages
    page_num = i
    url = 'first part of url' + str(page_num) + 'last part of url'
    driver.get(url)

#export to csv
pd['text'] = content
pd.to_csv('scrape.csv')
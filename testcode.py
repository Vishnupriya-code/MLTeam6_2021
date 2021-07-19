from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs 
from urllib.request import urlopen
import requests
import urllib.request
url = 'https://forums.tapas.io/'
driver = webdriver.Chrome()
driver.get(url)
whatinput = driver.find_element_by_id('search-term')
whatinput.send_keys('Memes')
findbutton = driver.find_element_by_xpath('//*[@id="ember800"]/header/div/div/div[2]/div/div/div/div/div[2]/div[1]/a')
findbutton.click()
title_element = driver.find_elements_by_xpath('//*[@id="ember1182"]/div[2]')[0]
titlename = title_element.text
print(titlename)
user_message = driver.find_elements_by_xpath('//*[@id="ember1182"]/div[3]')[0]
comment = user_message.text
print(comment)
date_element = driver.find_elements_by_xpath('//*[@id="ember1182"]/div[2]/div[2]/div[2]/span[1]/span')[0]
date = date_element.text
print(date)
category_element = driver.find_elements_by_xpath('//*[@id="ember1182"]/div[2]/div[2]/div[1]/div/a/span[2]')[0]
categoryname = category_element.text
print(categoryname)
comments = pd.DataFrame(columns = ['Stuff']) 
ids = driver.find_elements_by_xpath("//*[contains(@id,'ember1182')]") 

comment_ids = []
for i in ids:
    comment_ids.append(i.get_attribute('id'))

for x in comment_ids:
    
        date_element = driver.find_elements_by_xpath('//*[@id="' + x +'"]/div[50]')[0]
        date = date_element.text
   
    #Adding date, userid and comment for each user in a dataframe    
comments.loc[len(comments)] = [date]
csv_data = comments.to_csv()  
print('\nCSV String Values:\n', csv_data)  
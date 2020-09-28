#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time


# In[2]:


links = []
base = 'https://cookpad.com/us/search/milkshakes?page='
for i in range(12):
    links.append(base + str(i + 1))
links


# In[3]:


recipes = []
driver = webdriver.Chrome(executable_path = 'C:\Drivers\Chrome_driver\chromedriver')
for link in links:
    driver.get(link)
    time.sleep(3)
    driver.maximize_window()
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
    temp = soup.find_all('a', class_ = 'media')
    temp = [i['href'] for i in temp]
    for i in temp:
        recipes.append(i)
driver.close()
recipes = list(set(recipes))
recipes


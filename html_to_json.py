#!/usr/bin/env python
# coding: utf-8

# In[156]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import re
from scipy import stats
import time
from selenium.common.exceptions import TimeoutException


# In[157]:


f = open(r'C:\Users\manke\Desktop\Dataset_confmake\Links_neurips_2022.txt', "r")
data = f.read()


# In[158]:


data = data.split("\n")


# In[159]:


data


# In[160]:


len(data)


# In[176]:


paper_json = {}

#for i in range(len(data)):
#   url = data[i]
    

url = data[0]

session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

initial_xpath = '/html/body/div/div[3]/div/div/main/div'
time.sleep(2)
forum = session.find_element(By.XPATH, initial_xpath)
new = forum.find_elements(By.XPATH,"./*")

attr = new[0].find_elements(By.XPATH, "./*")

paper_json["Title"] = attr[0].find_element(By.XPATH, "./h2/span").text

Author = attr[2].find_elements(By.XPATH, "./span/a")

auth_name = []
for name in Author:
    auth_ = name.text
    auth_name.append(auth_)
    
paper_json["Authors"] = auth_name


paper_json["Keyword"] = attr[4].find_element(By.XPATH, "./span[2]").text


paper_json["tldr"] = attr[5].find_element(By.XPATH, "./span[2]").text


paper_json["Abstract"] = attr[6].find_element(By.XPATH, "./span[2]").text


print(paper_json)

#/html/body/div/div[3]/div/div/main/div/div[3]/div[1]/div[1]/div[5]/span[2]

#name = innr_attr[0].find_elements(By.XPATH, "./*")
#print(name)

#/html/body/div/div[3]/div/div/main/div/div[1]/div[1]/h2

#for element in new:
 #   attr = element.find_element(By.XPATH,"./*")
  #  print(attr)


# In[173]:


import urllib.request, json 
with urllib.request.urlopen("https://api.openreview.net/notes?forum=09QFnDWPF8") as url2:
    contr = json.load(url2)


# In[177]:


paper_json["PaperDecision"] = contr["notes"][0]["content"]["decision"]
print(paper_json)


# In[180]:


review = list()
contr["notes"].pop(0)
for note in contr["notes"]:
    review.append(note["content"])
    
paper_json["Review"] = review

print(paper_json)


# In[182]:


contr["notes"][-1]["content"]["title"]


# In[183]:


contr["notes"][-1]["content"]["title"]


# In[ ]:





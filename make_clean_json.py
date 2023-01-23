#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import re
from scipy import stats
import time
from selenium.common.exceptions import TimeoutException
all_links = list()
import json


# In[361]:


dset = open('RAWjsondataset_clean.json')
data2 = json.load(dset)


# In[35]:


data[0]["Decision"] = data[0]['Review'][0]['decision']


# In[37]:


del data[0]['Review'][0]['decision']


# In[39]:


for i in range(1, len(data)):
    try:
        data[i]["Decision"] = data[i]['Review'][0]['decision']
        del data[i]['Review'][0]['decision']
    except:
        pass


# In[78]:


data


# In[47]:


for i in range(len(data)):
    for y in range(len(data[i]["Review"])):
        try:
            if re.search('Final Decision|final decision', data[i]["Review"][y]["title"]):
                data[i]["Metareview"] = data[i]["Review"][y]["comment"]
                del data[i]["Review"][y]["comment"]
        except:
            pass


# In[75]:


for i in range(len(data)):
        for k in range(len(data[i]["Review"])):
            try:
                if "metareview" in data[i]["Review"][k]:
                    data[i]["Metareview"] = data[i]["Review"][k]["metareview"]
                    del data[i]["Review"][k]["metareview"]
            except:
                pass


# In[98]:


search_string = data[81]['Title']
search_string = search_string.replace(' ', '+') 

url = "https://www.google.com/search?q=" + search_string + '+openreview' + "&start="
session = webdriver.Chrome()
session.implicitly_wait(10)
session.get(url)
matched_elements = session.get(url)
search_cont_xpath = '/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div'
search_cont = session.find_element(By.CSS_SELECTOR, ".v7W49e")
child = search_cont.find_elements(By.CSS_SELECTOR,".MjjYud")[0]
xpath = "//div[@class='MjjYud'][1]//div[@class='yuRUbf'][1]/a"
acc_url = session.find_element(By.XPATH, xpath).get_attribute("href")
acc_url


# In[20]:


xpath = '/html/body/div[8]/div/div[11]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[1]/div'


# In[130]:


session = webdriver.Chrome()
session.implicitly_wait(10)
start = 0

for i in range(7167, 7519):
    search_string = data[i]['Title']
    search_string = search_string.replace(' ', '+') 

    url = "https://www.google.com/search?q=" + search_string + '+openreview' + "&start="
    session.get(url)
    matched_elements = session.get(url)
    search_cont_xpath = '/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div'
    search_cont = session.find_element(By.CSS_SELECTOR, ".v7W49e")
    child = search_cont.find_elements(By.CSS_SELECTOR,".MjjYud")[0]
    xpath = "//div[@class='MjjYud'][1]//div[@class='yuRUbf'][1]/a"
    time.sleep(2)
    try:
        acc_url = session.find_element(By.XPATH, xpath).get_attribute("href")
    except:
        start = i
        break
    data[i]["URL"] = acc_url
    time.sleep(2)
    


# In[306]:


session = webdriver.Chrome()
session.implicitly_wait(10)

for i in range(7446, len(data1)): 
    try:  
        search_string = data1[i]["URL"]
        if "/pdf?id=" in search_string:
            search_string = search_string.replace("/pdf?id=", "/forum?id=" )
        session.get(search_string)
        xpath = '/html/body/div/div[3]/div/div/main/div/div[1]/div[4]/div[1]/span[2]'
        venue = session.find_element(By.XPATH, xpath).text
        data1[i]["Venue"] = venue
        
    except:
        self_input = input("type venue")
        data1[i]["Venue"] = self_input


# In[177]:


data[308]["ID"] = "RqCC_00Bg7V"


# In[174]:


data[597]["ID"] = "Vd7lCMvtLqg"


# In[302]:


i


# In[134]:


data1 = data[:7519]


# In[305]:


data1[7446]["ID"] = "nJ6e-3M2rx"


# In[310]:


file_name = "RAWjsondataset_clean.json"
final_thing = json.dumps(data1)
with open(file_name, 'w') as f:
    json.dump(data1, f, indent=2)


# In[138]:


data1[0]


# In[309]:


for i in range(len(data1)):
    for y in range(len(data1[i]["Review"])):
        try:
            if re.search('Paper Decision|paper decision', data1[i]["Review"][y]["title"]):
                del data1[i]["Review"][y]
        except:
            pass


# In[143]:


data1[0]


# In[150]:


for i in range(len(data1)):
    data1[i]["ID"] = data1[i]["URL"][32:]


# In[156]:


data1[500]


# In[153]:


data_sample = data1[:11]


# In[154]:


file_name = "cleandatasample_metareview.json"
final_thing = json.dumps(data_sample)
with open(file_name, 'w') as f:
    json.dump(data_sample, f, indent=2)


# In[355]:


data2[0]


# In[354]:


len(data2)


# In[320]:


reviews_to_delete = [review for review in data2[0]["Review"] if "comment" in review]
for review in reviews_to_delete:
    data2[0]["Review"].remove(review)


# In[362]:


for i in range(len(data2)):
    reviews_to_delete = [review for review in data2[i]["Review"] if "comment" in review]
    for review in reviews_to_delete:
        data2[i]["Review"].remove(review)


# In[382]:


file_name = "cleandatasetfull.json"
final_thing = json.dumps(data2)
with open(file_name, 'w') as f:
    json.dump(data2, f, indent=2)


# In[364]:


for i in range(len(data2)):
    review_list = data2[i]["Review"]
    for review in review_list:
        review_text = ""
        keys_to_combine = ["summary", "strengths_and_weaknesses", "limitations"]
        for key in keys_to_combine:
            if key in review:
                review_text += review[key] + " "
                del review[key]
        review["review2"] = review_text


# In[371]:


for i in range(1, len(data2)):
    reviews = data2[i]["Review"]
    for review in reviews:
        if review.get("review2") == "":
            del review["review2"]


# In[381]:


data2[4000]


# In[378]:


for i in range(len(data2)):
    reviews = data2[i]["Review"]
    for review in reviews:
        if "review2" in review:
            review["review"] = review.pop("review2")


# In[ ]:





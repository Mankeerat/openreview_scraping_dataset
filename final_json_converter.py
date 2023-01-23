#!/usr/bin/env python
# coding: utf-8

# In[82]:


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


# In[305]:


f = open(r'C:\Users\manke\Desktop\Dataset_confmake\Links_CoRL2022.txt', "r")
data = f.read()
data


# In[306]:


data = data.split("\n")


# In[307]:


ids = list()
for link in data:
    ids.append(link)
len(ids)


# In[204]:


all_links = all_links + ids


# In[205]:


len(all_links)


# In[94]:


import requests
import urllib.request, json 
final_json = list()
for i in all_links:
    url = 'https://api.openreview.net/notes?forum='+i
    print(url)
    #urllib.request.urlopen
    with urllib.request.urlopen(url) as url2:
        contr = json.load(url2)
    paper_json = {}
    try:
        paper_json["Title"] = contr["notes"][-1]["content"]["title"]
        paper_json["Authors"] = contr["notes"][-1]["content"]["authors"]
        paper_json["Keywords"] = contr["notes"][-1]["content"]["keywords"]
        paper_json["tldr"] = contr["notes"][-1]["content"]["TL;DR"]
        paper_json["Abstract"] = contr["notes"][-1]["content"]["abstract"]
        paper_json["PaperDecision"] = contr["notes"][0]["content"]["decision"] 

        review = list()
        contr["notes"].pop(0)
        contr["notes"].pop(-1)
        for note in contr["notes"]:
            review.append(note["content"])

        paper_json["Review"] = review
        time.sleep(0.)
        final_json.append(paper_json)
    except:
        pass
        

final_json


# In[217]:


import requests
import urllib.request, json 
final_json = list()
for i in all_links[17589:]:
    url = 'https://api.openreview.net/notes?forum='+i
    print(url)
    #urllib.request.urlopen
    with urllib.request.urlopen(url) as url2:
        contr = json.load(url2)
    paper_json = {}
    try:
        paper_json["Title"] = contr["notes"][-1]["content"]["title"]
        paper_json["Authors"] = contr["notes"][-1]["content"]["authors"]
        paper_json["Abstract"] = contr["notes"][-1]["content"]["abstract"]
        review = list()
        contr["notes"].pop(-1)
        for note in contr["notes"]:
            review.append(note["content"])

        paper_json["Review"] = review
        #time.sleep(0.)
        final_json.append(paper_json)
    except:
        pass

#final_json


# In[218]:


len(final_json)


# In[219]:


file_name = "finaljsondataset.json"
final_thing = json.dumps(final_json)
with open(file_name, 'a') as f:
    json.dump(final_json, f, indent=2)


# In[76]:


a = open('final_neurips2022.json')
b = open('final_neurips_2021.json')
c = open('final_iclr2023.json')
d = open('final_iclr2022.json')
e = open('final_ewsc+midl.json')
f = open('final_CoRL2022.json')

data = json.load(a)
data1 = json.load(b)
data2= json.load(c)
data3 = json.load(d)
data4 = json.load(e)
data5 = json.load(f)


complete_json = {}


# In[77]:


complete_json["NeurIps_2022"] = data
complete_json["Neurips_2021"] = data1
complete_json["iclr_2023"] = data2
complete_json["iclr_2022"] = data3
complete_json["CoRL2022.json"] = data5
complete_json["Eswc+midl+miccai.json"] = data4


# In[78]:


len(complete_json)


# In[79]:


file_name = "final_papers_review.json"
final_thing = json.dumps(complete_json)
with open(file_name, 'w') as f:
    json.dump(complete_json, f, indent=2)


# In[196]:


f = open(r'C:\Users\manke\Desktop\Dataset_confmake\api_metareview.txt', "r", encoding= 'utf-8')
data = f.read()


# In[197]:


#data = data.split("}, ")
data = data.split("\'forum\': ")
data


# In[198]:


ids = list()
for link in data:
    ids.append(link[1:12])
ids.pop(0)
ids


# In[68]:


import requests
import urllib.request, json 
final_json = list()
for i in ids:
    url = 'https://api.openreview.net/notes?forum='+i
    print(url)
    #urllib.request.urlopen
    with urllib.request.urlopen(url) as url2:
        contr = json.load(url2)
    paper_json = {}
    try:
        paper_json["Title"] = contr["notes"][-1]["content"]["title"]
        paper_json["Authors"] = contr["notes"][-1]["content"]["authors"]
        paper_json["Abstract"] = contr["notes"][-1]["content"]["abstract"]
        review = list()
        contr["notes"].pop(0)
        contr["notes"].pop(-1)
        for note in contr["notes"]:
            review.append(note["content"])

        paper_json["Review"] = review
        #time.sleep(0.)
        final_json.append(paper_json)
    except:
        pass

final_json


# In[69]:


len(final_json)


# In[70]:


file_name = "final_ewsc+midl.json"
final_thing = json.dumps(final_json)
with open(file_name, 'w') as f:
    json.dump(final_json, f, indent=2)


# In[3]:


dset = open('finaljsondataset.json')


# In[4]:


data = json.load(dset)


# In[5]:


data1 = data[3422:]


# In[6]:


data1[0]["Review"][0]["comment"]


# In[28]:


if data1[7154]["Review"][0]["title"] == "Final Decision":
    print('yes')


# In[183]:


len(data1)


# In[8]:


data1[9000]["Review"][1]["metareview"]


# In[286]:


len(data1[9000]["Review"][1]["metareview"])
remove = []
keep = []


# In[139]:


for i in range(15461):
    print(i)
    for y in range(len(data1[i]["Review"])):
        print(y)
        flag = False
        if re.search('Final Decision|final decision', data1[i]["Review"][y]["title"]) and len(data1[i]["Review"][y]["title"])<40:
            if len(data1[i]["Review"][y]["comment"])>140:
                flag = True
                keep.append(i)
                break
            else:
                remove.append(i)
            if flag == True:
                break
        if y == len(data1[i]["Review"]) - 1:
            remove.append(i)
        if flag == True:
            break


# In[247]:


for i in range(15461):
    print(i)
    for y in range(len(data1[i]["Review"])):
        print(y)
        flag = False
        try:
            if re.search('Final Decision|final decision', data1[i]["Review"][y]["title"]) and len(data1[i]["Review"][y]["title"])<40:
                if len(data1[i]["Review"][y]["comment"])>140:
                    flag = True
                    keep.append(i)
                    break
                else:
                    flagg = True
                    remove.append(i)
                    break
                if flag == True:
                    break
                if flagg == True:
                    break
            if y == len(data1[i]["Review"]) - 1:
                remove.append(i)
            if flagg == True:
                break
            if flagg == True:
                break
        except:
            for k in range(len(data1[i]["Review"])):
                flag1 = False
                flag2 = False
                if "metareview" in data1[i]["Review"][k]:
                    if len(data1[i]["Review"][k]["metareview"])>140:
                        flag1 = True
                        keep.append(i)
                        break
                    else:
                        flag2 = True
                        remove.append(i)
                        break
                    if flag1 == True:
                        break
                    if flag2 == True:
                        break
                if k == len(data1[i]["Review"]) - 1:
                    remove.append(i)
                if flag1 == True:
                    break
                if flag2 == True:
                    break


# In[287]:


for i in range(15461):
    print(i)
    for y in range(len(data1[i]["Review"])):
        print(y)
        flag = False
        flagg = False
        try:
            if re.search('Final Decision|final decision', data1[i]["Review"][y]["title"]) and len(data1[i]["Review"][y]["title"])<40:
                if len(data1[i]["Review"][y]["comment"])>140:
                    flag = True
                    keep.append(i)
                    break
                else:
                    flagg = True
                    remove.append(i)
                    break
                if flag == True:
                    break
                if flagg == True:
                    break
            if y == len(data1[i]["Review"]) - 1:
                remove.append(i)
            if flagg == True:
                break
            if flagg == True:
                break
        except:
            print("bruh")
            remove.append(i)
            break
        '''finally:
            for k in range(len(data1[i]["Review"])):
                flag1 = False
                flag2 = False
                if "metareview" in data1[i]["Review"][k]:
                    if len(data1[i]["Review"][k]["metareview"])>140:
                        flag1 = True
                        keep.append(i)
                        break
                    else:
                        flag2 = True
                        remove.append(i)
                        break
                    if flag1 == True:
                        break
                    if flag2 == True:
                        break
                if k == len(data1[i]["Review"]) - 1:
                    remove.append(i)
                if flag1 == True:
                    break
                if flag2 == True:
                    break'''


# In[288]:


len(keep)


# In[289]:


len(remove)


# In[290]:


seen = set()
uniq = [x for x in keep if x not in seen and not seen.add(x)]   
uniq


# In[291]:


seen1 = set()
uniq2 = [x for x in remove if x not in seen1 and not seen1.add(x)]   
uniq2


# In[292]:


result = [i for i in uniq if i in uniq2]
len(result)


# In[298]:


remove1 = []
keep1 = []
for num in uniq2:
        for k in range(len(data1[num]["Review"])):
                flag1 = False
                flag2 = False
                if "metareview" in data1[num]["Review"][k]:
                    if len(data1[num]["Review"][k]["metareview"])>140:
                        flag1 = True
                        keep1.append(num)
                        break
                    else:
                        flag2 = True
                        remove1.append(num)
                        break
                    if flag1 == True:
                        break
                    if flag2 == True:
                        break
                if k == len(data1[num]["Review"]) - 1:
                    remove1.append(num)
                if flag1 == True:
                    break
                if flag2 == True:
                    break


# In[299]:


len(keep1)


# In[300]:


len(remove1)


# In[301]:


seen = set()
le = [x for x in keep1 if x not in seen and not seen.add(x)]   
le


# In[302]:


seen1 = set()
be = [x for x in remove1 if x not in seen1 and not seen1.add(x)]   
be


# In[303]:


result = [i for i in uniq if i in uniq2]
len(result)


# In[309]:


len(keep)


# In[310]:


len(remove1)


# In[311]:


remove1


# In[316]:


keep_json = list()
for i in keep:
    keep_json.append(data1[i])


# In[317]:


len(keep_json)


# In[318]:


file_name = "keepcleanjson.json"
final_thing = json.dumps(keep_json)
with open(file_name, 'w') as f:
    json.dump(keep_json, f, indent=2)


# In[333]:


import numpy as np
#idx_keep = []
idx_keep = np.array(keep) + 3422
idx_keep = list(idx_keep)
idx_keep.sort()
idx_keep


# In[329]:





# In[312]:


data1[2990]["Review"]


# In[93]:


if re.search('Final Decision|final decision', data1[6079]["Review"][0]["title"]):
            if len(data1[6079]["Review"][0]["comment"])>140 or len(data1[6079]["Review"][0]["metareview"])>140:
                print('yes')


# In[243]:


for k in range(len(data1[8793]["Review"])):
    if "metareview" in data1[8793]["Review"][k]:
        print("yes")
keep1 = []
remove1 = []


# In[244]:


i = 15335
for y in range(len(data1[i]["Review"])):
    print(y)
    flag = False
    try:
        if re.search('Final Decision|final decision', data1[i]["Review"][y]["title"]) and len(data1[i]["Review"][y]["title"])<40:
            if len(data1[i]["Review"][y]["comment"])>140:
                flag = True
                keep1.append(i)
                break
            else:
                flagg = True
                remove1.append(i)
                break
            if flag == True:
                break
            if flagg == True:
                break
        if y == len(data1[i]["Review"]) - 1:
            remove1.append(i)
        if flagg == True:
            break
        if flagg == True:
            break
    except:
        print("bruh")
    finally:
        for k in range(len(data1[i]["Review"])):
            flag1 = False
            flag2 = False
            if "metareview" in data1[i]["Review"][k]:
                if len(data1[i]["Review"][k]["metareview"])>140:
                    flag1 = True
                    keep1.append(i)
                    break
                else:
                    flag2 = True
                    remove1.append(i)
                    break
                if flag1 == True:
                    break
                if flag2 == True:
                    break
            if k == len(data1[i]["Review"]) - 1:
                remove1.append(i)
            if flag1 == True:
                break
            if flag2 == True:
                break


# In[245]:


keep1


# In[ ]:





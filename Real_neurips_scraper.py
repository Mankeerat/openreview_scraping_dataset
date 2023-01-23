#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import re
from scipy import stats
import time
from selenium.common.exceptions import TimeoutException


# In[27]:


links = []


# In[36]:


#accepted-papers > ul
url = 'https://openreview.net/group?id=NeurIPS.cc/2022/Conference'

session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/ul'

for i in range(54):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        links.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[13]/a').click()
    time.sleep(2)


# In[38]:


with open('Links_neurips.txt', 'w') as f:
    for i in links:
        f.write(i)
        f.write('\n')


# In[41]:


seen = set()
uniq = [x for x in links if x not in seen and not seen.add(x)]   
uniq


# In[42]:


len(uniq)


# In[43]:


with open('Links_neurips.txt', 'w') as f:
    for i in uniq:
        f.write(i)
        f.write('\n')


# In[51]:


url = 'https://openreview.net/group?id=NeurIPS.cc/2022/Conference#rejected-papers-opted-in-public'

rejected_link = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[3]/ul'

for i in range(4):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        rejected_link.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[3]/nav/ul/li[7]/a').click()
    time.sleep(2)


# In[52]:


seen = set()
uniq_reject = [x for x in rejected_link if x not in seen and not seen.add(x)]   
uniq_reject


# In[53]:


len(uniq_reject)


# In[55]:


with open('Links_rejected_neurips.txt', 'w') as f:
    for i in uniq_reject:
        f.write(i)
        f.write('\n')


# In[60]:


url = 'https://openreview.net/group?id=NeurIPS.cc/2022/Track/Datasets_and_Benchmarks'

track_link = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/ul'

for i in range(7):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        track_link.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[10]/a').click()
    time.sleep(2)


# In[61]:


seen = set()
uniq_track = [x for x in track_link if x not in seen and not seen.add(x)]   
uniq_track


# In[62]:


len(uniq_track)


# In[64]:


with open('Links_rejected_neurips.txt', 'w') as f:
    for i in uniq_track:
        f.write(i)
        f.write('\n')


# In[69]:


url = 'https://openreview.net/group?id=NeurIPS.cc/2021/Conference#oral-presentations'

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/ul'

for i in range(3):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[6]/a').click()
    time.sleep(2)


# In[70]:


seen = set()
uniq_oral = [x for x in oral2021 if x not in seen and not seen.add(x)]   
uniq_oral


# In[71]:


len(uniq_oral)


# In[72]:


with open('Links_neurips_2021.txt', 'w') as f:
    for i in uniq_oral:
        f.write(i)
        f.write('\n')


# In[74]:


url = 'https://openreview.net/group?id=NeurIPS.cc/2021/Conference#spotlight-presentations'

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[3]/ul'

for i in range(12):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[3]/nav/ul/li[13]/a').click()
    time.sleep(2)


# In[77]:


seen = set()
uniq_oral = [x for x in oral2021 if x not in seen and not seen.add(x)]   
uniq_oral


# In[78]:


with open('Links_rejected_neurips.txt', 'w') as f:
    for i in uniq_oral:
        f.write(i)
        f.write('\n')


# In[79]:


url = 'https://openreview.net/group?id=NeurIPS.cc/2021/Conference#poster-presentations'

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[4]/ul'


for i in range(92):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[4]/nav/ul/li[13]/a').click()
    time.sleep(2)


# In[81]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
len(uniq_poster)


# In[82]:


with open('Links_rejected_neurips.txt', 'w') as f:
    for i in uniq_poster:
        f.write(i)
        f.write('\n')


# In[83]:


url = 'https://openreview.net/group?id=NeurIPS.cc/2021/Conference#rejected-papers-opted-in-public'

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[5]/ul'

for i in range(92):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[5]/nav/ul/li[9]/a').click()
    time.sleep(2)


# In[84]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
len(uniq_poster)


# In[85]:


with open('Links_rejected_neurips.txt', 'w') as f:
    for i in uniq_poster:
        f.write(i)
        f.write('\n')


# In[86]:


url = 'https://openreview.net/group?id=NeurIPS.cc/2021/Track/Datasets_and_Benchmarks/Round1'

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/ul'

for i in range(92):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[6]/a').click()
    time.sleep(2)


# In[87]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
len(uniq_poster)


# In[88]:


with open('Links_rejected_neurips.txt', 'w') as f:
    for i in uniq_poster:
        f.write(i)
        f.write('\n')


# In[90]:


url = 'https://openreview.net/group?id=ICLR.cc/2023/Conference#all-submissions'
#/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[13]/a

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/ul'

for i in range(81):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[13]/a').click()
    time.sleep(2)


# In[92]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
uniq_poster


# In[93]:


with open('ICLR_2023_links.txt', 'w') as f:
    for i in uniq_poster:
        f.write(i)
        f.write('\n')


# In[94]:


url = 'https://openreview.net/group?id=ICLR.cc/2023/Conference#withdrawn-submissions'
#/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[13]/a

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[3]/ul'

for i in range(19):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[3]/nav/ul/li[13]/a').click()
    time.sleep(2)


# In[96]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
len(uniq_poster)


# In[97]:


with open('Links_rejected_neurips.txt', 'w') as f:
    for i in uniq_poster:
        f.write(i)
        f.write('\n')


# In[98]:


url = 'https://openreview.net/group?id=ICLR.cc/2023/Conference#desk-rejected-submissions'
#/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[13]/a

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[4]/ul'

for i in range(19):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[3]/nav/ul/li[13]/a').click()
    time.sleep(2)


# In[99]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
len(uniq_poster)


# In[100]:


with open('Links_rejected_neurips.txt', 'w') as f:
    for i in uniq_poster:
        f.write(i)
        f.write('\n')


# In[101]:


url = 'https://openreview.net/group?id=ICLR.cc/2022/Conference#oral-submissions'
#/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[13]/a

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/ul'

for i in range(19):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[5]/a').click()
    time.sleep(2)


# In[102]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
len(uniq_poster)


# In[104]:


url = 'https://openreview.net/group?id=ICLR.cc/2022/Conference#spotlight-submissions'
#/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[13]/a

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[3]/ul'

for i in range(19):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[3]/nav/ul/li[7]/a').click()
    time.sleep(2)


# In[105]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
len(uniq_poster)


# In[106]:


with open('Links_rejected_neurips.txt', 'w') as f:
    for i in uniq_poster:
        f.write(i)
        f.write('\n')


# In[107]:


url = 'https://openreview.net/group?id=ICLR.cc/2022/Conference#poster-submissions'
#/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[13]/a

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[4]/ul'

for i in range(19):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[4]/nav/ul/li[13]/a').click()
    time.sleep(2)


# In[108]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
len(uniq_poster)


# In[109]:


with open('Links_rejected_neurips.txt', 'w') as f:
    for i in uniq_poster:
        f.write(i)
        f.write('\n')


# In[110]:


url = 'https://openreview.net/group?id=ICLR.cc/2022/Conference#submitted-submissions'
#/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[13]/a

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[5]/ul'

for i in range(31):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[5]/nav/ul/li[13]/a').click()
    time.sleep(2)


# In[111]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
len(uniq_poster)


# In[112]:


with open('Links_rejected_neurips.txt', 'w') as f:
    for i in uniq_poster:
        f.write(i)
        f.write('\n')


# In[113]:


url = 'https://openreview.net/group?id=ICLR.cc/2022/Conference#desk-rejected-withdrawn-submissions'
#/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[13]/a

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[6]/ul'

for i in range(17):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[6]/nav/ul/li[13]/a').click()
    time.sleep(2)


# In[114]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
len(uniq_poster)


# In[115]:


with open('Links_rejected_neurips.txt', 'w') as f:
    for i in uniq_poster:
        f.write(i)
        f.write('\n')


# In[148]:


url = 'https://openreview.net/group?id=ICLR.cc/2019/Conference#withdrawn-rejected-submissions'
#/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[13]/a

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[4]/ul'

for i in range(17):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[6]/nav/ul/li[13]/a').click()
    time.sleep(2)


# In[149]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
len(uniq_poster)


# In[150]:


with open('Links_rejected_neurips.txt', 'w') as f:
    for i in uniq_poster:
        f.write(i)
        f.write('\n')


# In[205]:


url = 'https://openreview.net/group?id=ICLR.cc/2013/conference#reject'
#/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[13]/a

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[6]/ul'

for i in range(2):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div/nav/ul/li[6]/a').click()
    time.sleep(2)


# In[206]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
len(uniq_poster)


# In[207]:


with open('Links_rejected_neurips.txt', 'w') as f:
    for i in uniq_poster:
        f.write(i)
        f.write('\n')


# In[21]:


url = 'https://openreview.net/group?id=aclweb.org/ACL/2020/Workshop/NLP-COVID#accepted-abstracts'
#/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[13]/a

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[3]/ul'

for i in range(6):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[3]/nav/ul/li[10]/a').click()
    time.sleep(2)


# In[22]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
len(uniq_poster)


# In[23]:


with open('Links_ACL2020_workshop.txt', 'a') as f:
    for i in uniq_poster:
        f.write(i)
        f.write('\n')


# In[92]:


url = 'https://openreview.net/group?id=thecvf.com/ECCV/2022/Workshop/VIPriors#accept--oral-poster-tbd-'
#/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[13]/a

oral2021 = []
session = webdriver.Chrome()
session.implicitly_wait(20)
session.get(url)

xpath = '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/ul'

for i in range(2):
    new_papers = session.find_element(By.XPATH, xpath)
    new = new_papers.find_elements(By.XPATH,"./*")
    for element in new:
        link = element.find_element(By.XPATH, "./h4/a[1]").get_attribute('href')
        oral2021.append(link)
        
    button = session.find_element(By.XPATH, '/html/body/div/div[3]/div/div/main/div/div[3]/div/div[2]/div[2]/nav/ul/li[5]/a').click()
    time.sleep(2)


# In[93]:


seen = set()
uniq_poster = [x for x in oral2021 if x not in seen and not seen.add(x)]   
len(uniq_poster)


# In[94]:


with open('ECCV2022.txt', 'a') as f:
    for i in uniq_poster:
        f.write(i)
        f.write('\n')


# In[ ]:





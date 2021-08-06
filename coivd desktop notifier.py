#!/usr/bin/env python
# coding: utf-8

# In[3]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier


# In[4]:


header = {"User-Agent":"Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/india/", headers = header)
html = urlopen(req)


# In[15]:



html.status


# In[25]:


total_case = obj.find("div",{"class":"maincounter-number"}).span.text.split()[0]


# In[26]:


new_cases = obj.find("li", {"class":"news_li"}).strong.text.split()[0]


# In[27]:


death = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]


# In[28]:



notifier = ToastNotifier()


# In[39]:



message  = "New Cases - "+ new_cases+" and Death - "+death+" and total case - "+total_case


# In[40]:


message


# In[41]:



notifier.show_toast(title="COVID-19 Update", msg=message, duration=5, icon_path=r"virus.ico")


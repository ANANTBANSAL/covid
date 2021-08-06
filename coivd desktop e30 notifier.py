#!/usr/bin/env python
# coding: utf-8

# In[7]:


from urllib.request import urlopen, Request
import bs4
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier
import threading
import time
import plyer


# In[8]:


def get_html_data():
    header = {"User-Agent":"Mozilla"}
    req = Request("https://www.worldometers.info/coronavirus/country/india/", headers = header)
    html = urlopen(req)
    return html


# In[9]:


def get_corona_detail_of_india():
    html = get_html_data() 
    obj=bs(html)
    total_case = obj.find("div",{"class":"maincounter-number"}).span.text.split()[0]
    new_cases = obj.find("li", {"class":"news_li"}).strong.text.split()[0]
    death = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]
    message  = "New Cases - "+ new_cases+" and Death - "+death+" and total case - "+total_case  
    return message


# In[10]:


# function for notifying...
def notify_me():
    while True:
        plyer.notification.notify(
            title="COVID 19 cases of INDIA",
            message=get_corona_detail_of_india(),
            timeout=10,
            
        )
        time.sleep(30)


# In[11]:


# create a new thread
th1 = threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()


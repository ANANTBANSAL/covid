#!/usr/bin/env python
# coding: utf-8

# In[13]:


from urllib.request import urlopen, Request
import bs4
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier
import threading
import time
import plyer
import smtplib as s
from email.mime.text import MIMEText


# In[14]:


ob = s.SMTP("smtp.gmail.com",587)


# In[15]:


ob.starttls()


# In[16]:


ob.login("ravizc109@gmail.com","zc109@gmail.com")


# In[17]:


def get_html_data():
    header = {"User-Agent":"Mozilla"}
    req = Request("https://www.worldometers.info/coronavirus/country/india/", headers = header)
    html = urlopen(req)
    return html


# In[18]:


def get_html_data():
    header = {"User-Agent":"Mozilla"}
    req = Request("https://www.worldometers.info/coronavirus/country/india/", headers = header)
    html = urlopen(req)
    return html


# In[19]:


def get_corona_detail_of_india():
    html = get_html_data() 
    obj=bs(html)
    total_case = obj.find("div",{"class":"maincounter-number"}).span.text.split()[0]
    new_cases = obj.find("li", {"class":"news_li"}).strong.text.split()[0]
    death = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]
    message  = "New Cases - "+ new_cases+" and Death - "+death+" and total case - "+total_case  
    return message


# In[ ]:


subject = "COVID 19 cases of INDIA today"


# In[20]:


# function for notifying...
def notify_me():
    while True:
        body = get_corona_detail_of_india()
        
        message = "Subject:{}\n\n{}".format(subject,body)
        listofaddress = ['anantbansal643091@gmail.com']
        ob.sendmail("ravizc109",listofaddress,message)
        time.sleep(2200)


# In[21]:


# create a new thread
th1 = threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()


# In[ ]:





# In[ ]:





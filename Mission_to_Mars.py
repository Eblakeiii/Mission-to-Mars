#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[2]:


# Windows users
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', r'C:\Users\eblak\Class_Folder\Mission-to-Mars', headless=False)


# In[3]:


# Visit the Quotes to Scrape site -------> used a shortened URL
url = 'https://rb.gy/fqggqy'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[ ]:


# Parse the HTML
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[10]:


slide_elem.find("div", class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[11]:


# Use the parent element to find the summary paragraph text for the first article
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### Featured images

# In[13]:


# set Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[14]:


# find and click the Full Image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[15]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[16]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[17]:


# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[18]:


# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# # Scraping a table using Pandas

# In[3]:


# create df of web table using pandas
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[4]:


type(df)


# In[5]:


df.columns


# In[6]:


df.index


# In[8]:


df.to_html()


# In[9]:


browser.quit()


# In[ ]:





from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd

# Windows users
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', r'C:\Users\eblak\Class_Folder\Mission-to-Mars', headless=False)

# Visit the site to Scrape site -------> used a shortened URL
url = 'https://rb.gy/fqggqy'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Parse the HTML
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')

slide_elem.find("div", class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the summary paragraph text for the first article
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

# set Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# find and click the Full Image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()

# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# # Scraping a table using Pandas
# create df of web table using pandas
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df

df.to_html()

# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# parse the main html with soup
html = browser.html
hemi_soup = soup(html, 'html.parser')
imgs = hemi_soup.find('div', class_="collapsible results")

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# a. loop for titles on main page
titles = []
for title in hemi_soup:
    titles.append(hemi_soup.find_all('h3'))
titles

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# b. Cerberus
browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
cerberus_html = browser.html
cerberus_soup = soup(cerberus_html, 'html.parser')

# find title
cerberus_title = cerberus_soup.find("h2", class_ = 'title').text

# Find the relative image url
cerberus = cerberus_soup.find('img', class_ = 'wide-image')
cerberus_img = cerberus['src']

# add base url to rel url
hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
cerberus_url = hemi_url + cerberus_img

print(cerberus_url)
print(cerberus_title)

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# c. Schiaparelli
browser.back()
browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
schiaparelli_html = browser.html
schiaparelli_soup = soup(schiaparelli_html, 'html.parser')

# find title
schiaparelli_title = schiaparelli_soup.find("h2", class_ = 'title').text

# find the relative image url
schiaparelli = schiaparelli_soup.find('img', class_ = 'wide-image')
schiaparelli_img = schiaparelli['src']

# add base url to rel url
hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
schiaparelli_url = hemi_url + schiaparelli_img

print(schiaparelli_url)
print(schiaparelli_title)

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# d. Syrtis Major
browser.back()
browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
syrtis_html = browser.html
syrtis_soup = soup(syrtis_html, 'html.parser')

# find title
syrtis_title = syrtis_soup.find("h2", class_ = 'title').text

# find the relative image url
syrtis = syrtis_soup.find('img', class_ = 'wide-image')
syrtis_img = syrtis['src']

# add base url to rel url
hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
syrtis_url = hemi_url + syrtis_img

print(syrtis_url)
print(syrtis_title)

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# e. Valles Marineris
browser.back()
browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
valles_html = browser.html
valles_soup = soup(valles_html, 'html.parser')

# find title
valles_title = valles_soup.find("h2", class_ = 'title').text

# find the relative image url
valles = valles_soup.find('img', class_ = 'wide-image')
valles_img = valles['src']

# add base url to rel url
hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
valles_url = hemi_url + valles_img

print(valles_url)
print(valles_title)

hemisphere_image_urls.clear()

b = {'img_url': cerberus_url, 'title': cerberus_title}
c = {'img_url': schiaparelli_url, 'title': schiaparelli_title}
d = {'img_url': syrtis_url, 'title': syrtis_title}
e = {'img_url': valles_url, 'title': valles_title}

hemisphere_image_urls.append(b)
hemisphere_image_urls.append(c)
hemisphere_image_urls.append(d)
hemisphere_image_urls.append(e)

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

browser.quit()


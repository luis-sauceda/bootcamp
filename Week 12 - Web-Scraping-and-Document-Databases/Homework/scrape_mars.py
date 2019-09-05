from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import time

def init_browser():
    # Retrieve page with the requests module and print response result
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

#def get_html(url, click):
    
#    browser.visit(url)
#    if click == True:
#        time.sleep(5)
#        browser.click_link_by_partial_text('FULL IMAGE')
        
#    html = browser.html
#    return bs(html, 'html.parser')

def scrape():
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    #soup = get_html(url, False)
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    slides =  soup.find_all('li', class_='slide')

    titles = []
    news_content = []

    for news in slides:
        titles.append(news.find('div', class_='content_title').text)
        news_content.append(news.a.text)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(url)
    time.sleep(5)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)

    html = browser.html
    soup = bs(html, 'html.parser')

    #soup = get_html(url, True)

    url = 'https://www.jpl.nasa.gov'
    image =  soup.find_all('img', class_='fancybox-image')[0]['src']
    featured_image_url = url + image
    #featured_image_url

    url = "https://twitter.com/marswxreport?lang=en"
    #soup = get_html(url, False)
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    #mars_weather

    tables = pd.read_html("https://space-facts.com/mars/")[1]
    #tables
    table = {}
    for index, row in tables.iterrows():
        table.update({row[0]:row[1]})

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    #soup = get_html(url, False)
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    url = 'https://astrogeology.usgs.gov'
    #images = soup.find_all('div', class_='description')
    images = soup.body.find_all('a', class_='product-item')
    source_imgs = []
    source_links = []
    img_titles = []
    #bol = False
    for image in images:
        img_lnk = url + image['href']
        title = image.text
        if img_lnk not in source_links:
            source_links.append(img_lnk)
        if title not in img_titles:
            if title != "":
                img_titles.append(title)
        

    for link in source_links:
        browser.visit(link)
        soup = bs(browser.html, 'html.parser')
        large_image = url + soup.find_all('img', class_='wide-image')[0]['src']
        source_imgs.append(large_image)
        time.sleep(5)

    hemisphere_image_urls = []
    cont = 0
    for source in source_imgs:
        hemisphere_image_urls.append({"title": img_titles[cont], "img_url": source})
        cont += 1
    #hemisphere_image_urls
    mars_data = {
                "news_titles" : titles,
                "news_content": news_content,
                "featured_image": featured_image_url, 
                "mars_weather": mars_weather,
                "mars_table": table,
                "hemisphere_images": hemisphere_image_urls
                }
    return mars_data

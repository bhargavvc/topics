


import requests
from bs4 import BeautifulSoup
import scrapy

# before executing these scripts run pipenv shell and pipenv install

def using_beautifulsoup(url):
    # Web Scraping using BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # u cant all heading and tiles and paragram be specifing the tag
    titles = soup.find_all('h2')
    
    for title in titles:
        print(title.text)

url = 'https://www.bbc.co.uk/news'
# using_beautifulsoup(url)


from selenium import webdriver

def using_selenium(url):
    
    
    driver = webdriver.Chrome()
    driver.get(url)
    print(driver.title)
    driver.quit()

url = 'https://www.bbc.co.uk/news'
using_selenium(url)


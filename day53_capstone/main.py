import re
import time

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

FORM_URL ='https://docs.google.com/forms/d/e/1FAIpQLSf5t_-XN3nGdL-y9msCYo70c2k6bA9i_ep2byMRJATL6Wanpg/viewform?usp=sf_link'
ZWILLO_URL = 'https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A37.842914%2C%22east%22%3A-122.32992%2C%22south%22%3A37.707608%2C%22west%22%3A-122.536739%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

chrome_driver_path = "Z:\Development\chromedriver\chromedriver-win64\chromedriver.exe"
service =Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #need this in order to keep browser open
driver = webdriver.Chrome(service=service, options=options)


response = requests.get(url=ZWILLO_URL, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

listing_links_elements = soup.findAll(name='a', class_ ="property-card-link")
all_links = []

for link in listing_links_elements:
    href = link.get("href")
    if "https://" in href:
        all_links.append(href)
    else:
        href = "https://www.zillow.com" + href
        all_links.append(href)

all_addresses = []
address_elements = soup.findAll(name='address')
for address in address_elements:
    all_addresses.append(address.text.split('|')[-1])

all_prices = []
pricing_elements = soup.findAll('span',{"data-test": "property-card-price"})
for price in pricing_elements:
    full_price = price.get_text().split('+')[0].split('/')[0]
    all_prices.append(full_price)

for i in range(len(all_links)):
    driver.get(FORM_URL)

    time.sleep(3)
    address = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')


    address.send_keys(all_addresses[i])
    price.send_keys(all_prices[i])
    link.send_keys(all_links[i])
    submit.click()


import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "Z:\Development\chromedriver\chromedriver-win64\chromedriver.exe"
service =Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #need this in order to keep browser open
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by="id",value="cookie")

items = driver.find_elements(by="css selector", value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_minutes = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:

        all_prices = driver.find_elements(by="css selector", value="#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split('-')[1].replace(",",""))
                item_prices.append(cost)

        upgrades = {}
        for n in range(len(item_prices)):
            upgrades[item_prices[n]] = item_ids[n]

        money = driver.find_element(by="id", value="money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        affordable_upgrades = {}
        for cost,id in upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        print(affordable_upgrades)
        highest_price_upgrade = max(affordable_upgrades)
        print(highest_price_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_upgrade]

        driver.find_element(by="id", value=to_purchase_id).click()

        timeout = time.time() + 5

        if time.time() > five_minutes:
            cookie_per_second = driver.find_element(by="id", value="cps").text
            print(cookie_per_second)
            break
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "Z:\Development\chromedriver\chromedriver-win64\chromedriver.exe"
service =Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #need this in order to keep browser open
driver = webdriver.Chrome(service=service, options=options)

# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# whole_price = driver.find_element(by="class name", value="a-price-whole")
# fraction_price = driver.find_element(by="class name", value="a-price-fraction")
# price = float(whole_price.text) + float(fraction_price.text)/100
# print(price)
driver.get("https://www.python.org/")
event_times = driver.find_elements(by="css selector", value=".event-widget time")
event_names = driver.find_elements(by='css selector', value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] ={
        "time":event_times[n].text,
        "name": event_names[n].text
    }
print(events)


















# driver.close()this will close tab that chrome opened
# driver.quit()this will quit from all of chrome
# driver.quit()
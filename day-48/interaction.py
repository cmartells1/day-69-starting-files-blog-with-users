from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "Z:\Development\chromedriver\chromedriver-win64\chromedriver.exe"
service =Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #need this in order to keep browser open
driver = webdriver.Chrome(service=service, options=options)


# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# total_articles = driver.find_element(by="css selector", value="#articlecount a")
# # total_articles.click()
#
# # all_portals = driver.find_element(by="link text", value="All portals") # This is how you would find an element by link text
# # all_portals.click()
#
# search_button = driver.find_element(by="css selector", value="#p-search a")
# search_button.click()
#
# search = driver.find_element(by="name", value="search")
# search.click()
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(by="name", value='fName')
first_name.send_keys("Chris")

last_name = driver.find_element(by="name", value="lName")
last_name.send_keys("Martells")

email = driver.find_element(by="name", value="email")
email.send_keys("test@hotmail.com")

sign_up_btn = driver.find_element(by="class name", value="btn")
sign_up_btn.click()
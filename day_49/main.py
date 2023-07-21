import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "Z:\Development\chromedriver\chromedriver-win64\chromedriver.exe"
service =Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #need this in order to keep browser open
driver = webdriver.Chrome(service=service, options=options)


driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3632363015&f_AL=true&f_WT=2&geoId=101174742&keywords=developer&location=Canada&refresh=true")
time.sleep(5)
driver.find_element(by="class name", value="cta-modal__primary-btn").click()

driver.find_element(by="id", value="username").send_keys("cmartells2@gmail.com")
driver.find_element(by="id", value="password").send_keys("mayakevin3")
driver.find_element(by="class name", value="btn__primary--large").click()


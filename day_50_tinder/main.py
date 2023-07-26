from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from time import sleep

FB_EMAIL = 'martells.test@gmail.com'
FB_PASSWORD = 'pythonbigtasstic'

chrome_driver_path = "Z:\Development\chromedriver\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # need this in order to keep browser open
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(by='xpath',
                                   value='//*[@id="q-881491550"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

sleep(2)
facebook_login = driver.find_element(by="xpath",
                                     value='//*[@id="q1685094670"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(by='id', value='email')
email.send_keys(FB_EMAIL)
password = driver.find_element(by='id', value='pass')
password.send_keys(FB_PASSWORD)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
allow_location_button = driver.find_element(by="xpath",
                                            value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element(by="xpath",
                                           value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element(by="xpath", value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

# Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    # Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element(by="xpath",
                                          value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div['
                                                '1]/div/div[2]/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(by="css selector", value=".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()

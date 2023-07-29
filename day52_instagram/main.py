import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "Z:\Development\chromedriver\chromedriver-win64\chromedriver.exe"
service =Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #need this in order to keep browser open
# driver = webdriver.Chrome(service=service, options=options)

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = 'jmartells780'
PASSWORD = 'pythonbigtasstic'

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service, options=options)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')

        try:

            time.sleep(2)
            username = self.driver.find_element(by='xpath', value='//*[@id="loginForm"]/div/div[1]/div/label/input')
            username.send_keys(USERNAME)

            password = self.driver.find_element(by='xpath', value='//*[@id="loginForm"]/div/div[2]/div/label/input')
            password.send_keys(PASSWORD)

            login_button = self.driver.find_element(by='xpath', value='//*[@id="loginForm"]/div/div[3]/button')
            login_button.click()

            time.sleep(5)
            not_now = self.driver.find_element(by='xpath', value='//*[@id="mount_0_0_3V"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div')
            not_now.click()

            time.sleep(5)
            not_now2 = self.driver.find_element(by='xpath', value='//*[@id="mount_0_0_3c"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
            not_now2.click()
        except NoSuchElementException:
            print('Element not found')

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element(by='xpath', value=
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(by='xpath', value='/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(by='css selector', value="li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by='xpath', value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


follower = InstaFollower()
follower.login()
follower.find_followers()
follower.follow()
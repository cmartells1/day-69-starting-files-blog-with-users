from time import sleep
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

CHROME_DRIVER_PATH = "Z:\Development\chromedriver\chromedriver-win64\chromedriver.exe"
PROMISED_DOWN = 940
PROMISED_UP = 940
TWITTER_EMAIL ="cmartells2@gmail.com"
TWITTER_PASSWORD = "pythonbigtasstic"

SERVICE =Service(executable_path=CHROME_DRIVER_PATH)
OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_experimental_option("detach", True) #need this in order to keep browser open
# driver = webdriver.Chrome(service=service, options=options)

class InternetSpeedTwitterBot:
    def __init__(self, service, options):
        self.driver = webdriver.Chrome(service=service, options=options)
        self.up =0
        self.down=0


    def get_internet_speed(self):
        # self.driver.get('https://www.speedtest.net/')
        # sleep(10)
        #
        # go_button = self.driver.find_element(by='class name', value='start-text')
        # go_button.click()
        #
        # sleep(60)
        # self.down = float(self.driver.find_element(by='class name', value='download-speed').text)
        # self.up = float(self.driver.find_element(by='class name', value='upload-speed').text)
        # print(f"Download speed is {self.down} \n and upload speed is {self.up}")
        pass

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/login')
        sleep(3)

        email = self.driver.find_element(by='xpath', value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.click()
        email.send_keys(TWITTER_EMAIL)

        ok_button = self.driver.find_element(by='xpath', value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        ok_button.click()

        sleep(10)

        password = self.driver.find_element(by='xpath', value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)

        tweet_space = self.driver.find_element(by='xpath', value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_space.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element(by='xpath'
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        sleep(2)
        self.driver.quit()

speed_bot = InternetSpeedTwitterBot(SERVICE, OPTIONS)
speed_bot.get_internet_speed()
speed_bot.tweet_at_provider()
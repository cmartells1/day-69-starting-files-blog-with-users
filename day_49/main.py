import time

from selenium import webdriver
from selenium.common import NoSuchElementException
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

all_listings = driver.find_element(by="css selector",value=".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element(by="css selector",value=".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element(by="class name",value="fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys("7802882401")

        submit_button = driver.find_element(by="css selector",value="footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(by="class name",value="artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(by="class name",value="artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(by="class name",value="artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

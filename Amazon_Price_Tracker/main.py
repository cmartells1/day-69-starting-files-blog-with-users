import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}
MY_EMAIL = "martells.test@gmail.com"
PASSWORD = "ecyuossjrgzzehyo"
BUY_PRICE = 200

response  = requests.get(url=URL, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").getText()
split_price = price.split("$")[1]
price_as_float = float(split_price)
print(price_as_float)
title = soup.find(id="productTitle").getText().strip()
print(title)

if price_as_float< BUY_PRICE:
    message = f"{title} is now ${price_as_float}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8"))


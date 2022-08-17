# import smtplib
#
# my_email = "martells.test@gmail.com"
# password = "kbrjybvetpgzyhnh"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="martells.test@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email"
#                         )

import datetime as dt
import random
import smtplib

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)
#
# date_of_birth = dt.datetime(year=1985, month=10, day=3)

MY_EMAIL = "martells.test@gmail.com"
PASSWORD = "kbrjybvetpgzyhnh"

now = dt.datetime.now()
today = now.weekday()
quote_list = []

if today == 2:
    with open(file="quotes.txt", mode="r") as data:
        quote_list = data.readlines()
        quote = random.choice(quote_list)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="martells.test@yahoo.com",
                            msg=f"Subject:Quote of the day\n\n{quote}"
                            )

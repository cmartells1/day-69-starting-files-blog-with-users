##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib


MY_EMAIL = "martells.test@gmail.com"
PASSWORD = "kbrjybvetpgzyhnh"

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthday_data = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month

for birthday in birthday_data:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    if birthday["month"] == month and birthday['day'] == day:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_data:
            letter = letter_data.read()
            birthday_letter = letter.replace("[NAME]", birthday["name"])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthday["email"],
                                msg=f"Subject: Happy Birthday!!\n\n{birthday_letter}")




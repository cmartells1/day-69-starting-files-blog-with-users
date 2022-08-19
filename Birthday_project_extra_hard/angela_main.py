import smtplib
from datetime import datetime
import pandas
import random

MY_EMAIL = "martells.test@gmail.com"
PASSWORD = "kbrjybvetpgzyhnh"

today=datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
# new_dict = {new_key:new_value for (index, data_row) in data.iterrows()}
# birthday_dict = {
#     (birthday_month, birthday_day) : data_row
# }
birthday_dict = {(data_row.month,data_row.day):data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    print(type(birthday_dict[today_tuple]))
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
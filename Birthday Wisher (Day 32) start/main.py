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

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(year)

date_of_birth = dt.datetime(year=1985, month=10, day=3)
from twilio.rest import Client
import smtplib

TWILIO_SID = "ACdcf18e261639dc91a6da0288ee00e9d2"
TWILIO_AUTH_TOKEN = "6e0a2a96475356d00a118999788f2add"
TWILIO_NUMBER = "+18302713512"
TWILIO_SEND_NUMBER = "+1 780 288 2401"

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "martells.test@gmail.com"
PASSWORD = "kbrjybvetpgzyhnh"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=TWILIO_SEND_NUMBER
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
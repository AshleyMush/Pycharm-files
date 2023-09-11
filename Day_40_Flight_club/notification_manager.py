from twilio.rest import Client
import smtplib

TWILIO_SID = 'AC6f116151d21a4d82a76413bc5f07b6ca'
TWILIO_AUTH_TOKEN  = 'b498a4bb728a1093d016af30fa804f80'
TWILIO_VIRTUAL_NUMBER = '+447883304338'
TWILIO_VERIFIED_NUMBER='+447478881797'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        my_email = "Opportunityhubzw@Gmail.Com"
        password = "vmlvmqygizoyuesv"

        receiver = "Email2_Test@Yahoo.Com"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=receiver,
                                msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                                )


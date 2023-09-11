import smtplib
from user_manager import User_Manager
from otp_generator import OTP_Generator
from email.mime.text import MIMEText
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.environ.get("my_email")
password = os.environ.get("password")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")


print(f"{my_email}\n"
      f"{password}\n"
      f"{account_sid}\n"
      f"{auth_token}\n")

class Notification_Manager():
    """
    A class to handle sending notifications, both SMS and email.
    Provides methods to send verification OTPs.
    """

    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.username = self.user_manager.firstname
        self.OTP_generator = OTP_Generator()


    def send_sms(self, receiving_phone_number):
        """
        Sends an SMS notification containing an OTP.

        Parameters:
            receiving_phone_number (str): The phone number to send the OTP to.
        """
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f'Your verification code is: {self.OTP_generator.generate_pin()}',
            from_='+447883304338',
            to=receiving_phone_number
        )
        print(message.status)

    def send_email(self, receiving_email):
        """
        Sends an email notification containing an OTP.

        Parameters:
            receiving_email (str): The email address to send the OTP to.
        """
        email_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif;">
                <h2 style="color: #4CAF50;">Welcome to MY WEBSITE, {self.username}!</h2>
                <p>Your one-time passcode (OTP) is:</p>
                <h3 style="background-color: #f2f2f2; padding: 10px; display: inline-block;">{self.OTP_generator.generate_password()}</h3>
                <p>Enter the OTP now to continue logging in.</p>
            </body>
        </html>
        """

        msg = MIMEText(email_content, 'html')
        msg['From'] = my_email
        msg['To'] = receiving_email
        msg['Subject'] = "One-time-passcode (OTP)"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            try:
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=receiving_email, msg=msg.as_string())
            except smtplib.SMTPAuthenticationError:
                print("SMTP Authentication Error")



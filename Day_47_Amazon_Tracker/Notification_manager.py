"""
This script defines a Notification_Manager class that is used to send email notifications.
It uses environment variables to securely manage sensitive information such as authentication tokens and passwords.
"""

import smtplib
from email.mime.text import MIMEText
import os

my_email = "Opportunityhubzw@Gmail.Com"
password = os.environ.get("password")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")




class Notification_Manager:
    """
    This class is responsible for sending notification emails. It is initialized with the lowest price of a product
    and contains a method to send an email notification with details about the price drop.
    """

    def __init__(self, LOWEST_PRICE):
        """
        Initialize the Notification_Manager with the lowest price of a product.

        Args:
        LOWEST_PRICE (float): The lowest price of the product to include in the notification email.
        """
        self.lowest_price = LOWEST_PRICE
        self.link_to_product = "https://www.amazon.com/iPhone-13-Pro-256GB-Graphite/dp/B0BGYBX3LK/ref=sr_1_1?crid=2DA5GYPTFSPWT&keywords=iphone%2B14&qid=1694167126&sprefix=iphone%2B14%2Caps%2C224&sr=8-1&th=1"

    def send_email(self, receiving_email):
        """
        Sends a formatted email notification containing the lowest price and a message.

        Args:
        receiving_email (str): The email address to send the notification to.

        Raises:
        smtplib.SMTPAuthenticationError: If authentication to the SMTP server fails.
        """
        email_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif;">
                <h2 style="color: #4CAF50;">Hey, The iphone 13 is now going at {self.lowest_price}!</h2>
                <a href="{self.link_to_product}>Follow This link to buy it</a>
                <h1 style="background-color: #f2f2f2; padding: 10px; display: inline-block;">${self.lowest_price}</h1>

                <p>Price Alert the </p>
            </body>
        </html>
        """

        msg = MIMEText(email_content, 'html')
        msg['From'] = my_email
        msg['To'] = receiving_email
        msg['Subject'] = "IPhone 13 price drop udemy day 47 challenge"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            try:
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=receiving_email, msg=msg.as_string())
            except smtplib.SMTPAuthenticationError:
                print("SMTP Authentication Error")

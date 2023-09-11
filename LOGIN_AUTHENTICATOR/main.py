from user_manager import User_Manager
from notification_manager import Notification_Manager


"""
main.py

This module serves as the primary entry point for the user authentication application. 
It initializes the User_Manager class, captures user inputs for personal details, 
and then validates the user's email address and phone number using the Validator class.

Functionality:
    1. Initialize the User_Manager and prompt the user for their personal details.
    2. Validate the provided email and phone number.

Dependencies:
    - user_manager: Contains the User_Manager class which handles user-related operations.
"""

#TODO ADD PASSWORD

user_manager = User_Manager()
user_manager.create_user()
username = user_manager.firstname
print(username)

validated_email = user_manager.validate_user_email()
validated_number  = user_manager.validate_user_number()


notification_manager = Notification_Manager(user_manager=user_manager)
notification_manager.send_email(validated_email)
notification_manager.send_sms(validated_number)



user_pin_received = input("Enter The 6 digit pin you received:\n ")
user_email_received = input("Paste the magic password you received:\n")


print(f"Welcome {username}")
print(f"Validated Email: {validated_email}")
print(f"Validated Phone Number: {validated_number}")

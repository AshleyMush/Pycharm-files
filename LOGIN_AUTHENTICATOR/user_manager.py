from validator import Validator

"""
This module contains the User_Manager class, responsible for capturing user data and handling 
user-related operations.

Functionality:
    1. Capture user details.
    2. Validate user's email and phone number.

Classes:
    - User_Manager: A class that handles user creation, input capture, and validation.
"""
class User_Manager:
    """
    This class handles user-related operations, including user creation and validation.
    """

    def __init__(self):
        """
        Initializes the User_Manager class by printing a welcome message.
        """
        self.validator = Validator()  # Creating an instance of Validator within User_Manager
        print("Welcome to Ashley's log in page.")

    def create_user(self):

        self.firstname = input("What's your first name?\n").title()
        self.last_name = input("What's your last name?\n").title()

        self.email1 = input("Enter your email address: \n").title()
        self.email2 = input("Type email again: \n").title()
        self.region_code = input("Enter your region e.g, GB for Great Britain, US for United States:\n").upper()
        self.phone_number = input("Enter your valid phone number:\n")

    def validate_user_email(self):
        validated_email = self.validator.validate_email(self.email1)
        return validated_email

    def validate_user_number(self):
        validated_phone_number = self.validator.validate_phone_number(self.phone_number, self.region_code)
        return validated_phone_number








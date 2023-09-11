import phonenumbers
import re

"""
validator.py

This module contains the Validator class which is responsible for validating user data, 
specifically email addresses and phone numbers.

Dependencies:
    - phonenumbers: A Python library for parsing, formatting, storing, and validating international phone numbers.
    - re: A module that provides support for regular expressions (aka. regex).

Classes:
    - Validator: A class that provides methods to validate email addresses and phone numbers.
"""

class Validator:
    """
    A class to validate user's email and phone number.

    Attributes:
        valid_email (str): A validated email address.
        valid_phone_number (str): A validated phone number.
    """

    def __init__(self):
        """
        Constructs the Validator class with initial empty values for validated email and phone number.
        """
        self.valid_email = ''
        self.valid_phone_number = ''

    def validate_email(self, email_to_validate):
        """
              Validates an email address using a regex pattern.

              Parameters:
                  email_to_validate (str): The email address to be validated.

              Returns:
                  str: If the email is valid, returns the email. Otherwise, returns an appropriate error message.
              """

        try:
            # Define a regular expression pattern to match valid email addresses.
            regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            if bool(re.match(regex, email_to_validate)):
                self.valid_email = email_to_validate
            else:
                return "Invalid email format"

            return self.valid_email

        except re.error:
            return "Please enter a valid email."

        except TypeError as e:
            return f"{e} Please enter a valid email. The email you provided is not a string."

        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def validate_phone_number(self, phone_number, country_code):
        """
            Validates a phone number based on the provided country code.

            Parameters:
                phone_number (str): The phone number to be validated.
                country_code (str): The country code corresponding to the phone number, e.g. 'US' for United States.

            Returns:
                str: If the phone number is valid, returns the phone number with its country code. Otherwise, returns an appropriate error message.
        """

        try:
            parsed_number = phonenumbers.parse(phone_number, country_code)
            if phonenumbers.is_valid_number(parsed_number):
                # Format the number with the country code and return it
                self.valid_phone_number = phonenumbers.format_number(parsed_number,
                                                                     phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                return self.valid_phone_number
            else:
                return "Invalid phone number"

        except phonenumbers.NumberParseException as e:
            if e.error_type == phonenumbers.NumberParseException.INVALID_COUNTRY_CODE:
                return "The provided country code is invalid."
            elif e.error_type == phonenumbers.NumberParseException.NOT_A_NUMBER:
                return "The provided input is not a number."
            elif e.error_type == phonenumbers.NumberParseException.TOO_SHORT_AFTER_IDD:
                return "The phone number is too short after the international dialing prefix."
            elif e.error_type == phonenumbers.NumberParseException.TOO_SHORT_NSN:
                return "The phone number is too short to be a valid number for the given region."
            else:
                return f"An unexpected error occurred: {e}"



import string
import random

class OTP_Generator:
    '''
    returns a random int or random string object
    '''

    def __init__(self):
        self.otp_pin = ''
        self.otp_pw = ''

    def generate_pin(self, length=6):
        """
        param length: TYPE int: This is for setting the length of the desired pin
        :return: string which will be the user one time pin
        """
        characters = string.digits  # Use only digits
        for _ in range(length):
            self.otp_pin += random.choice(characters)
        pin = int(self.otp_pin)
        return pin

    def generate_password(self, length=16):
        """
        :param length: TYPE int: This is for setting the length of the desired password
        :return: string which will be the user one time password
        """
        characters = string.ascii_letters  # use letters only
        for _ in range(length):
            self.otp_pw += random.choice(characters)
        password = self.otp_pw
        return password



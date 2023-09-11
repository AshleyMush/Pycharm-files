""""

I want to generate a random 6 digit OTP, store it in my sheet and send it to  my phone number

a person will create a new user, they will enter their name, email, phone number, the person's created password will be compared.
    if the passwords match:
        the program will generate an random_OTP (OTP_MANAGER)
        an SMS of the random_OTP  will be sent to the user using twilio (NOTIFICATION_MANAGER)
        the person will have to input the OTP
        if random_OTP == OTP:
            user_name and user_pw will be posted to the data_sheet (DATA_MANAGER)
        else:
            invalid

"""

import string
import random

class OTP_Generater():
    def __init__(self):
        self.PIN = ''
        self.PW = ''
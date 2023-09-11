import smtplib
import datetime as dt
import random

my_email = "Opportunityhubzw@Gmail.Com"
password = "vmlvmqygizoyuesv"

receiver = "Email2_Test@Yahoo.Com"



#____________Getting hold current time___________#

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()

print(day_of_the_week)

# date_of_birth = dt.datetime(year=1998, month=6, day=14)
#
# print(date_of_birth)

#Look =s at a particular date and time and it
#___________Accessing Quotes__________
file_path = "quotes.txt"

if day_of_the_week == 2:

    with open(file_path, "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
#_____________SMTP EMAIL_______________________________#

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver,
                            msg=f"SUBJECT:Today's Motivational Quote\n\n" + quote)

#TODO
"""
TODO
- store data in Json file 
-Get hold of dictionary[name] from list of names use mail merging

"""



#Password Generator Project

import random
import  secrets  #This generates cryptographically strong random numbers, which can generate security tokens, make passwords, ensure account authentication, etc.


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")


nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = '' #Define an empty string that will take up all the elements we will loop

for char in range(1,nr_letters +1): # =1 because If the user enters 4, that's a range from 1-4 with range in python this is 1-3


#random_char = secrets.choice(letters) This is much more secure

 password += random.choice(letters) #SHORTER You can still use Secret

for sym in range(1, nr_symbols+1):

 password += random.choice(symbols)

for num in range(1, nr_numbers+1):

 password += random.choice(numbers)

print(f"Your New password is: {password}\nThis password is not strong, for stronger password see Strong password")




'''

#Combining all lists
password = letters + numbers + symbols


#Initiate the iterator
single_letter = 0


#Use secrets.choice() to pick a secure random letter from the list

random_letter = secrets.choice(password)

for single_letter in password: #Generating random letters and then making them a string


    single_letter += random_letter

    #print(single_letter, end='')  # end ='' is added to convert for loop into horizontal, it's basically an empty string









#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P



'''
'''
 Use secrets.choice() to pick a random letter from the list

random_letter = secrets.choice(letters)
print(random_letter)

'''


'''

'''
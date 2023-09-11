alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount, first_choice):
# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#We'll need a for loop for each letter
#We'll need a new position variable
#We'll need to store each letter in a string

    cypher_text = ""
#H
#E
#L
#L
#O

    for each_letter in plain_text:
#we want to find the index of each letter
        position = alphabet.index(each_letter) #Index of 'H' in alphabet = 7

#Add shift value to it
#           12         7         (input value = 5)
        new_position =position + shift_amount

#         L                         12
        new_letter = alphabet[new_position]
#THIS IS IN A FOR LOOP SO IT'S FOCUSSING ON LETTER BY LETTER.

#Add that to our storage which is cypher_text
        cypher_text += new_letter






    print(f"Your encoded text is {cypher_text}")





encrypt(plain_text=text, shift_amount=shift, first_choice=direction)



# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

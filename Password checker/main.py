global password

password = ""

password_vault = []

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']






initial_password = input("Please enter your new password: ")
password_check = input("Please re-enter your password: ")

if initial_password == password_check:
    print("Password correct!")

    actuval_password = initial_password
    password_vault.append(actuval_password)

    #TODO :Add function for what ever program you'll use this for
    password = initial_password
else:
    print("Passwords do not match.")

    tries = 3

    while tries > 0:
        guess = input("Please enter your password: ")

        if guess == password:
            print("Password correct!")
            break
        else:
            tries -= 1
            print("Password incorrect. You have", tries, "tries left.")

    if tries == 0:
        print("Too many tries. Please try again later.") #TODO : Add timer for this function so that it gives the user the time they'll need to try again



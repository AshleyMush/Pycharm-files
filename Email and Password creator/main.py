import re


def is_valid_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r"[^@]+@[^@]+\.[^@]+"

    # Return True if the email matches the pattern, False otherwise
    return re.match(pattern, email) is not None


def new_user( initial_email, email_check):
    email_address = ""
    email_vault = []

    password = ""
    password_vault = []

    #Checking email stage

    if initial_email == email_check:
        if is_valid_email(initial_email):
            print("Email correct!")
            verified_email = initial_email
            email_vault.append(verified_email)  # TODO 1 : This is where I will store all user's emails  vault this and make it only accessible to you




            # TODO :Add function for whatever program you'll use this for
            email_address += initial_email

            #Checking password stage

            initial_password = input("Please enter your new password:\n")
            password_check = input("Please re-enter your password:\n")


            if initial_password == password_check:
                print("Password correct!")
                actual_password = initial_password
                password_vault.append(actual_password)  # TODO : This is where I will store all user's passwords

                # TODO :Add function for whatever program you'll use this for
                password += initial_password
            else:
                print("Passwords do not match.")
                password_tries = 2
                while password_tries > 0:
                    guess = input("Please re-enter your password: ")
                    if guess == initial_password:
                        print("Password correct!")
                        break
                    else:
                        password_tries -= 1
                        print("Password incorrect. You have", password_tries, "tries left.")
                if password_tries == 0:
                    print("Too many tries! If you have forgotten your password. Please Click 'forgotten password'")
                    # TODO : Add timer for this function so that it gives the user the time they'll need to try again

        else:
            print("Invalid email address, here's an example of a valid emaail address 'johndoe@email.com.")
            email_tries = 2
            while email_tries > 0:
                email_guess = input("Please re-enter your email address: ").lower()
                if email_guess == initial_email:
                    if is_valid_email(initial_email):
                        print("Valid email address!")

                        initial_password = input("Please enter your new password:\n")
                        password_check = input("Please re-enter your password:\n")

                        if initial_password == password_check:
                            print("Password correct!")
                            actual_password = initial_password
                            password_vault.append(actual_password)  # TODO : This is where I will store all user's passwords

                            # TODO :Add function for whatever program you'll use this for
                            password += initial_password
                        else:
                            print("Passwords do not match.")
                            password_tries = 2
                            while password_tries > 0:
                                guess = input("Please re-enter your password: ")
                                if guess == initial_password:
                                    print("Password correct!")
                                    break
                                else:
                                    password_tries -= 1
                                    print("Password incorrect. You have", password_tries, "tries left.")
                            if password_tries == 0:
                                print(
                                    "Too many tries! If you have forgotten your password. Please Click 'forgotten password'")
                                # TODO : Add timer for this function so that it gives the user the time they'll need to try again

                else:
                    email_tries -= 1
                    print("Email address incorrect. Check for any uppercase, symbols or special characters in your email address and try again.")

            if email_tries == 0:
                print("Too many tries! If you have forgotten your email address. Please Click 'forgotten email address' or create a new account.")
                # TODO : Add timer for this function so that it gives the user the time they'll need to try again



    else:
        print("Email address does not match.")
        email_tries = 2
        while email_tries > 0:
            email_guess = input("Please re-enter your email address: ").lower()
            if email_guess == initial_email:
                if is_valid_email(initial_email):
                    print("Email address correct!")

                    initial_password = input("Please enter your new password:\n")
                    password_check = input("Please re-enter your password:\n")

                    if initial_password == password_check:
                        print("Password correct!")
                        actual_password = initial_password
                        password_vault.append(actual_password)  # TODO : This is where I will store all user's passwords

                        # TODO :Add function for whatever program you'll use this for
                        password += initial_password
                    else:
                        print("Passwords do not match.")
                        password_tries = 2
                        while password_tries > 0:
                            guess = input("Please re-enter your password: ")
                            if guess == initial_password:
                                print("Password correct!")
                                break
                            else:
                                password_tries -= 1
                                print("Password incorrect. You have", password_tries, "tries left.")
                        if password_tries == 0:
                            print("Too many tries! If you have forgotten your password. Please Click 'forgotten password'")
                            # TODO : Add timer for this function so that it gives the user the time they'll need to try again

            else:
                email_tries -= 1
                print("Email address incorrect. Check for any uppercase, symbols or special characters in your email address and try again.")
        if email_tries == 0:
            print("Too many tries! If you have forgotten your email address. Please Click 'forgotten email address' or create a new account.")
            # TODO : Add timer for this function so that it gives the user the time they'll need to try again

initial_email = input("Please enter your email address:\n").lower()

if is_valid_email(initial_email):

 email_check = input("Please re-enter your email address:\n").lower()

else:
    print("Invalid email address, here's an example of a valid email address 'johndoe@email.com.")
    email_tries = 3
    while email_tries > 0:
        email_check = input("Please re-enter your email address: ").lower()
        if email_check == initial_email:
            if is_valid_email(initial_email):
                print("Valid email address!")

    if email_tries == 0:
        print("Too many tries! If you do not have an email address, please create one then try again later")









new_user( initial_email, email_check)
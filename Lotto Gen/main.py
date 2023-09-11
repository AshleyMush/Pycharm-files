import secrets

def return_to_menu():
    while True:
        menu = input("Return to main menu? (y/n)")
        if menu == "y":
            mainmenu()
            break
        elif menu == "n":
            print("Now exiting program, goodbye!")
            break
        else:
            print("Invalid input.")

def mainmenu():
    while True:
        print("Select a game you're playing")
        print("1. Euromillion")
        print("2. Thunderball")
        print("3. Lotto")
        print("4. Set for life")
        operation = input("Enter choice (1/2/3/4):\n")

        if operation == "1":
            print("Welcome to Euromillions:\n")
            main_numbers, lucky_stars = generate_euromillions_numbers()
            print("Main numbers: ", ", ".join(str(num) for num in main_numbers))
            print("Lucky stars: ", ", ".join(str(num) for num in lucky_stars))
            return_to_menu()

        elif operation == "2":
            print("Welcome to Thunderball:\n")
            main_numbers_thun, thunderball = generate_thunderball_numbers()
            print("Main numbers: ", ", ".join(str(num) for num in main_numbers_thun))
            print("Thunderball: ", ", ".join(str(num) for num in thunderball))
            return_to_menu()

        elif operation == "3":
            print("Welcome to Lotto:\n")
            main_numbers_lotto = generate_lotto_numbers()
            print("Main numbers: ", ", ".join(str(num) for num in main_numbers_lotto))
            return_to_menu()

        elif operation == "4":
            print("Welcome to Set for life:\n")
            main_numbers_set, lifeball = generate_set_for_life_numbers()
            print("Main numbers: ", ", ".join(str(num) for num in main_numbers_set))
            print("Life Ball: ", ", ".join(str(num) for num in lifeball))
            return_to_menu()

        else:
            print("Invalid input.")

def generate_euromillions_numbers():
    main_numbers = set()
    while len(main_numbers) < 5:
        main_numbers.add(secrets.randbelow(50) + 1)

    lucky_stars = set()
    while len(lucky_stars) < 2:
        lucky_stars.add(secrets.randbelow(10) + 1)
    return main_numbers, lucky_stars

def generate_thunderball_numbers():
    main_numbers_thun = set()
    while len(main_numbers_thun) < 5:
        main_numbers_thun.add(secrets.randbelow(39) + 1)

    thunderball = set()
    while len(thunderball) < 1:
        thunderball.add(secrets.randbelow(10) + 1)
    return main_numbers_thun, thunderball

def generate_set_for_life_numbers():
    main_numbers_set = set()
    while len(main_numbers_set) < 5:
        main_numbers_set.add(secrets.randbelow(47) + 1)

    lifeball = set()
    while len(lifeball) < 1:
        lifeball.add(secrets.randbelow(10) + 1)
    return main_numbers_set, lifeball

def generate_lotto_numbers():
    main_numbers_lotto = set()
    while len(main_numbers_lotto) < 6:
        main_numbers_lotto.add(secrets.randbelow(59) + 1)

    return main_numbers_lotto

mainmenu()

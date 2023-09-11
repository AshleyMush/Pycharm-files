import random

RANDOM_NAME = []
RANDOM_FOLLOWING = []


def celeb_generator():
    """This list will generate a random celeb string "Kim Kardashian" and following int 226000000 """
    global RANDOM_NAME, RANDOM_FOLLOWING

    celeb_list = [  # INDEX
        {"Selena Gomez": 226000000},  # 0
        {"Dwayne Johnson": 172000000, },  # 1
        {"Kylie Jenner": 156000000},  # 2
        {"Kim Kardashian": 194000000},
        {"Beyonce": 174000000},
    ]
    # {'Kim Kardashian': 194000000} This is what it currenlty is.
    Random_dictionary = random.choice(celeb_list)

    #                            key             value
    # Taking the key out from {'Kim Kardashian': 156000000} and putting it in a list then calling it at index 0 KEY = <class 'str'> VALUE = <class 'int'>
    RANDOM_NAME = list(Random_dictionary.keys())[0]
    RANDOM_FOLLOWING = list(Random_dictionary.values())[0]

    #         <class 'str'> <class 'int'>
    #       Kim Kardashian   1560000000
    return RANDOM_NAME, RANDOM_FOLLOWING


def play_again():
    """This function gives the option to play again or exit"""

    Play_again = input("Want to play again?\n Press 'Y' to play again or 'N' to exit.").lower()
    if Play_again == 'y':
        game()

    elif Play_again == 'n':
        return "Exiting"
    else:
        print("Invalid input.")
        play_again()


def game():
    '''This Function takes Random name and following as celeb1 then while the game isn't over generates a new value for celeb 2 and compares the celeb1 to celeb2. Finally celeb1 becomes cele2 because it's in a loop it generates a new number for celeb 2'''

    global RANDOM_NAME, RANDOM_FOLLOWING
    end_game = False

    # Selena Gomez
    celeb1_name = RANDOM_NAME
    # 17200000
    celeb1_following = RANDOM_FOLLOWING

    #   while   The game isn't over
    while not end_game:
        # Generate a new name and following
        celeb_generator()
        celeb2_name = RANDOM_NAME
        celeb2_following = RANDOM_FOLLOWING

        print(f"1️⃣ {celeb1_name} has {celeb1_following} followers")

        guess = input(
            f"2️⃣Is {celeb2_name}'s following on instagram higher or lower?\nType 'H' for higher or Type 'L' for lower.\n").lower()

        if guess == 'h':
            if celeb2_following > celeb1_following:
                print(f"✔️Correct! {celeb2_name} has more followers than {celeb1_name}")
                celeb2_name == celeb1_name
                celeb2_following == celeb1_following


            else:
                print("❌Incorrect, Better luck next time.")
                end_game = True
                play_again()


        elif guess == 'l':
            if celeb2_following < celeb1_following:
                print(f"✔️Correct, {celeb2_name} has less followers than {celeb1_name} ")
                celeb2_name == celeb1_name, celeb2_following == celeb1_following

            else:
                print("❌Incorrect, Better luck next time.")
                end_game = True
                play_again()



        else:
            print("Invalid Input,Type 'H' for higher or Type 'L' for lower.\n ")
            game()


game()
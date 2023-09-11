import random
from game_data import data
from art import logo, vs

RANDOM_NAME = ""
RANDOM_FOLLOWING = 0
RANDOM_DESCRIPTION = ""
RANDOM_COUNTRY = ""


def celeb_generator():
    """This list will generate a random celeb string "Kim Kardashian" and following int 226000000 """
    global RANDOM_NAME, RANDOM_FOLLOWING, RANDOM_DESCRIPTION, RANDOM_COUNTRY
    '''   {
            'name': 'Priyanka Chopra Jonas',
            'follower_count': 53,
            'description': 'Actress and musician',
            'country': 'India'
            }
         
    '''  # What it may look like
    Random_dictionary = random.choice(data)

    #            key             value
    '''   {
            'name': 'Priyanka Chopra Jonas',
            'follower_count': 53,
            'description': 'Actress and musician',
            'country': 'India'
            }

    '''  # Click Here to see what  the random dictionary may look like
    '''
inner_value = inner_dict["inner_key"]
    '''
    # Accessing a value within the inner dictionary

    RANDOM_NAME = Random_dictionary['name']
    RANDOM_FOLLOWING = Random_dictionary['follower_count']
    RANDOM_DESCRIPTION = Random_dictionary['description']
    RANDOM_COUNTRY = Random_dictionary['country']

    #         <class 'str'> <class 'int'>
    #       Kim Kardashian   1560000000
    # Click Here to see what the data looks like
    return RANDOM_NAME, RANDOM_FOLLOWING, RANDOM_DESCRIPTION, RANDOM_COUNTRY


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
    """This Function takes Random name and following as celeb1 then while the game isn't over generates a new value
    for celeb 2 and compares the celeb1 to celeb2. Finally celeb1 becomes cele2 because it's in a loop it generates a
    new number for celeb 2"""

    global RANDOM_NAME, RANDOM_FOLLOWING, RANDOM_DESCRIPTION, RANDOM_COUNTRY

    end_game = False
    # generate new random celeb details
    celeb_generator()
    celeb1_name = RANDOM_NAME
    celeb1_following = RANDOM_FOLLOWING
    celeb1_description = RANDOM_DESCRIPTION
    celeb1_country = RANDOM_COUNTRY

    #   while   The game isn't over generate new random celeb details
    while not end_game:
        celeb_generator()
        celeb2_name = RANDOM_NAME
        celeb2_following = RANDOM_FOLLOWING
        celeb2_description = RANDOM_DESCRIPTION
        celeb2_country = RANDOM_COUNTRY
        # If the details are equal then generate new random celeb details
        if celeb1_name == celeb2_name:
            celeb_generator()
            celeb2_name = RANDOM_NAME
            celeb2_following = RANDOM_FOLLOWING
            celeb2_description = RANDOM_DESCRIPTION
            celeb2_country = RANDOM_COUNTRY

        print(logo)

        print(
            f"Compare:1️⃣ {celeb1_name} a {celeb1_description} from {celeb1_country} who has {celeb1_following} followers")

        print(vs)

        guess = int(input(f"Against2️⃣:{celeb2_name} a {celeb2_description} from {celeb2_country}\nWho has more "
                          f"followers?\nType 1️⃣ {celeb1_name} or 2️⃣{celeb2_name}.\n"))

        if guess == 1:
            if celeb2_following > celeb1_following:
                print(f"✔️ Correct! {celeb2_name} has more followers than {celeb1_name}")
                celeb2_name = celeb1_name
                celeb2_following = celeb1_following
                celeb2_country = celeb1_country
                celeb2_description = celeb1_description
            else:
                print("❌ Incorrect. Better luck next time.")
                end_game = True
                play_again()

        elif guess == 2:
            if celeb2_following < celeb1_following:
                print(f"✔️ Correct! {celeb2_name} has fewer followers than {celeb1_name}")
                celeb2_name = celeb1_name
                celeb2_following = celeb1_following
                celeb2_country = celeb1_country
                celeb2_description = celeb1_description
            else:
                print("❌ Incorrect. Better luck next time.")
                end_game = True
                play_again()

        else:
            print("Invalid input. Type 'H' for higher or 'L' for lower.\n")
            game()


game()

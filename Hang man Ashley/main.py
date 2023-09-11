from replit import clear

import random

import hangman_art

import  hangman_words


print(hangman_art.logo)

def welcome():



    user_choice = input("\nWelcome to hangman!\n.\n1. Rules\n2. Game\nType exit to Exit\nType here 👉\n")

    if user_choice == "1" or user_choice == "1":
        rules()

    elif user_choice == "2" or user_choice == "2":
        game()

    elif user_choice.lower() == "exit":
        print("Exiting program.")
        return

    else:
        print("Invalid option. Type 'exit' to quit.")
        welcome()

def rules():
    print("_" * 180)  # Creating 180 underscores

    print("Guess the letters in the secret word to solve the puzzle.\nYou can guess a letter by typing it on your keyboard.\nYou'll score points for each correct letter you guess, and if you solve the word, you score for how fast you get it and how many chances you had left.\nGet the highest total score after 2 rounds to win the game and earn a trophy!🏆")
    print("_" * 180)

    rules_choice = input("\nType 1. to proceed to game\nType 'exit' to exit")
    if rules_choice == "1":
        welcome()

    elif rules_choice.lower() == "exit":
        print("Exiting program.")
        return

    else:
        print("Invalid option. Type 'exit' to quit.")
        rules()


def game():





    # GLOBAL ALLOWS YOU TO CALL UPON A VARIABLE REGARDLESS OF WHICH FUNCTION IT'S IN
    global chosen_word


    game_choice = input("Please select a category.\n1. Fruits (EASY)\n2. Vegetables (EASY)\n3. Random words (HARD)\nType here 👉")

    if game_choice == "1" or game_choice == "1":

        comp_choice = random.choice(hangman_words.fruits)  # Randomising any choice from fruits

        chosen_word = comp_choice.lower()

    elif game_choice == "2" or game_choice == "2":
        comp_choice = random.choice(hangman_words.vegetables)  # Randomising any choice from veggie

        chosen_word = comp_choice.lower()

    elif game_choice == "3":
        comp_choice = random.choice(hangman_words.word_list)

        chosen_word = comp_choice.lower()

    elif game_choice.lower() == "exit":
        print("Exiting program.")
        return

    else:
        print("Invalid option. Type 'exit' to quit.")
        welcome()

    # Print underscores to represent the unguessed letters of chosen_word
    word_length= len(chosen_word)


    # Set 'lives' to equal 6.

    lives = 6



    display = []

    for underscore in range(word_length):
        display+="_"

    print(chosen_word)
    end_of_game = False


    while not end_of_game:


        print(f"You have ❤️{lives} lives.")

        guess = input("Enter a letter.").lower() #Check Guessed letter

        clear()


        if guess in display:

            print(f"You've already guessed {guess}")




        for position in range(word_length): #Finding the position of the word le
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"You guess {guess} which is not in the word.")
            lives -= 1
            print(f"You have {lives} chances left.")

            if lives == 0:

                end_of_game = True
                print("Game Over!")





        # Then reduce 'lives' by 1.
        # If lives goes down to 0 then the game should stop and it should print "You lose."

            # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")


        # Check if user has got all letters.
        if "_" not in display:
            end_of_game == True

            print("🏆🏆🏆You win!🏆🏆🏆🏆")

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.


        print(hangman_art.stages[lives])

welcome()

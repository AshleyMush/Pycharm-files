#TODO Generate a random number
#Display the random number as a clue
#ask the user to guess a number and then compare the number to the random number
#Show if the number is hot or cold

#Give the user chances to guess and a level of difficulty

import random


'''
functions

def my_func(This_input):
    do this with This_input
    then do this with This_input
    
--call function--

my_function(This_input)

--to make it easy to call simply rename the call to a variable

variable = my_function(This_input)





'''

def lives(level_of_difficulty):


    if level_of_difficulty == 1:
        return 10
    else:
        return 5


def random_number_generator(minimum_range, maximum_range):

    for _ in range(1):
        random_figure= random.choice(range(minimum_range,maximum_range +1)) #I'm using + 1 because range(1,6) is   1, 2, 3 ,4 5

        return  random_figure



def game():

    minimum_range = int(input("What number do you want the guess to be from:\n"))
    maximum_range = int(input("What limit do you want the guess to be to:\n"))

    level_of_difficulty =int( input("Please select a level of difficulty.\nType 1. For Easy or Type 2. for Hard.\n"))

#______________I'm going to rename the function call to variables to make it easy for me call them________________

    #10
    chances = lives(level_of_difficulty)
    #45
    random_number = random_number_generator(minimum_range, maximum_range)

    print(f"Psst the answer is {random_number}.\n")

    guess = int(input(f"I am thinking of a number between {minimum_range} to {maximum_range}. Guess what it is!"))

    while chances > 0:
        if guess == random_number:
            return f"That's correct, the number was {random_number}"
        elif guess > random_number:
            chances -= 1
            print(f"too high, you have {chances} left")
        elif guess < random_number:
            chances -= 1
            print(f"too low, you have {chances} left")
        print(f"It's a number between {minimum_range} to {maximum_range}.")
        guess = int(input("Make a guess between 1-100: "))




    return play_again()



def play_again():
    option = input("You have run out of lives. Game over.\nType 'y' to play again or 'n' to exit").lower()

    if option == 'y':
        game()

    elif option == 'n':
        print("Now exiting, goodbye!")
    else:
        print("Invalid input.")
        play_again()


game()






































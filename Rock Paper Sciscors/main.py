import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


#My choice
choice_str= input("What do you choose?/n/n Type 0 for Rock. 1 For Paper or 2 for Paper.")

choice_int = int(choice_str)

#Convert the input into an int

print(choice_int)

player1_options = [rock, paper, scissors] #Store the gestures in a list

if player1_options[choice_int] == 0:
    print("You chose Rock.")
    print(player1_options[choice_int])

elif player1_options[choice_int] == 1:
    print("You chose Paper.")
    print(player1_options[choice_int])

elif player1_options[choice_int] == 2:
    print("You chose Scissors.")
    print(player1_options[choice_int])



#_________________________

#print(len(options)-1)

player2_options = [rock, paper, scissors]

computer_choice = random.randint(0, len(player2_options) -1)

if player2_options[computer_choice] == 0:
    print("Computer chose Rock.")
    print(player2_options[computer_choice])

elif player2_options[computer_choice] == 1:
    print("Computer chose Paper.")
    print(player2_options[computer_choice])

elif player2_options[computer_choice] == 2:
    print("Computer chose Scissors.")
    print(player2_options[computer_choice])


print(player2_options[computer_choice])



if (player1_options[choice_int] == rock and player2_options[computer_choice] == rock) or (player1_options[choice_int] == scissors and player2_options[computer_choice] == scissors) or (player1_options[choice_int] == paper and player2_options[computer_choice] == paper):
    print("It's a tie.")

elif (player1_options[choice_int] == rock and player2_options[computer_choice] == scissors) or (player1_options[choice_int] == scissors and player2_options[computer_choice] == rock) or (player1_options[choice_int] == scissors and player2_options[computer_choice] == paper) or (player1_options[choice_int] == paper and player2_options[computer_choice] == scissors) or (player1_options[choice_int] == rock and player2_options[computer_choice] == paper) or (player1_options[choice_int] == paper and player2_options[computer_choice] == rock):
    print("You win")
    
elif (player2_options[computer_choice]== rock and player1_options[choice_int] == scissors) or (player2_options[computer_choice]== scissors and player1_options[choice_int] == rock) or (player2_options[computer_choice]== scissors and player1_options[choice_int] == paper) or (player2_options[computer_choice]== paper and player1_options[choice_int] == scissors) or (player2_options[computer_choice]== rock and player1_options[choice_int] == paper) or (player2_options[computer_choice] == paper and player1_options[choice_int] == rock):
    print("You lost.")
    


#Store all these in lists
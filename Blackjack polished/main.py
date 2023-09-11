import  random


def deal_card():
    '''Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#We will use these two empy lists to store out decks

user_cards = []
computer_cards = []


#Use _ because we won't be needing this variable
for _ in range(2):

#ADD the dealt card into user_cards
    user_cards.append(deal_card())

    if len(user_cards)== 2:
        deal_card()
#We call deal card again because we want to restart the function and then keep computer_cards indented inline with the  twice for loop

    computer_cards.append(deal_card())

#TODO ADD THE COMPUTER'S SCORE AND USER'S SCORE

# Calculate the score for a given hand of cards
def calculate_score(cards):
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
        calculate_score()

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards)> 21:
        cards.remove(11)
        cards.append(1)
        if sum(cards)>21:
            calculate_score()
    #We return 0 because it represents blackjack in our game

    return sum(cards)

'''




computer_score = sum(computer_cards)

print(f"Computer score: {computer_score}.")

user_score = sum(user_cards)

print(f"Your score: {user_score}.")



#TODO CHECK  IF THEY HAVE A BLACKJACK (11,10) OR VICE VERSA

if computer_cards == [11,10] or computer_cards ==[10,11]:
    print("The computer has a blackjack, You lose.")

    # TODO ADD GAME OVER

    if user_cards == [11, 10] or user_cards == [10, 11]:


        print("You have a blackjack, You win.")

        # TODO ADD GAME OVER

        if computer_score > 21:
            print("Computer has gone over 21. You win.")

            #TODO ADD GAME OVER

        if user_score > 21:
            print("You went over 21. You lose.")

            # TODO ADD GAME OVER

draw_card = input("Would you like to deal another card?\nType 'y' to Deal or 'n' not to ").lower()

if draw_card == 'y':
    user_cards.append(deal_card())

else:
    computer_cards.append(deal_card())











'''

print(user_cards)
print(computer_cards)
import random

# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇


choice = input("Please select one\n\nHeads.\nTails.\n")

print(f"Your choice was {choice}")





prediction = random.randint(0, 1)

if prediction == 1:
    print("Head")


else:
    print("Tails")



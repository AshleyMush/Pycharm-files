# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

print(student_scores)

print(student_scores[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


highest_score = 0

for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"Highest score is {highest_score}")

'''
This part of the code is where you will write your solution to find the highest score in the list of student scores.

First, you initialize a variable highest_score to 0. This will be used to keep track of the highest score seen so far.

Then, you use a for loop to iterate through each score in student_scores. For each score, you check if it is greater than the current highest_score. If it is, then you update the highest_score variable to be equal to the score.

Finally, you print out the highest_score using an f-string to format the output message. This will display the highest score in the list of student scores.


'''
'''
___________________________Alternatively____________

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(highest_score)



'''
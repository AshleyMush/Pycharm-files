# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

#We converted the input into a list of strings

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#The list is now an int list




# 🚨 Don't change the code above 👆

#Finding the total student height

total_student_height = 0

number_of_students = 0


for height in student_heights:
  total_student_height += height

  #This will loop as many elements in student_heights
  number_of_students += 1



#Finding the average

average = round(total_student_height /number_of_students)

print(average)

'''

________________________-Alternatively__________________


total_height = sum(student_heights)
 number_of_students = len(student_heights)
 
 average = round(total_height/ len(student_height))
 
 print(average)


'''

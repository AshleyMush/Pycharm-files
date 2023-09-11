
'''
dictionary ={
"key a" : "This is key a",

"key b" : "This is key b"


}


#adding in dictionaries
dictionary["Key 1"]= "Value 1, can be an int."
_______________________________________________________________
#looping values
for value in dictionary:
 print(dictionary[value])
____________________________________________________
for key in dictionary:
  print(key)

  '''

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# Creating grades

# student_names = key      student = value     dict = {key: value}

student_grades = {}

for student in student_scores:
    score = student_scores[student]

    if score <= 70:

        #Adding to an empty dictionsry

        # DICTIONARY   [KEY]  =   "Value"
        student_grades[student] = "Fail"

    elif score <= 80:
        student_grades[student] ="Acceptable"

    elif score<= 90:
        student_grades[student] ="Exceeds expectation"

    elif score <= 100:
        student_grades[student] ="Outstanding"

print(student_grades)


# """
# You are going to use Dictionary Comprehension to create a dictionary called result that
# takes each word in the given sentence and calculates the number of letters in each word.
#
# """
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
#
# sentence_list = list(sentence.split())
#
# result = {word: len(word) for word in sentence_list}
#
# print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

#(temp_c * 9/5 ) + 32 = temp_f
# Write your code 👇 below:

# student_scores = {student: random.randint(1, 100) for student in names}

weather_f = {day: (temp* 1.8) + 32 for (day,temp ) in weather_c.items()}



print(weather_f)

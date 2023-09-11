# #FileNOTFOUND
#
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["ddfvd"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
#
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     raise TypeError("The message was made up ")

#
# height = float(input("Height:"))
# weight = int(input("Weight: "))
# if height > 3:
#     raise ValueError("Human height should not be over 3 meterrs.")
#
# bmi = weight / height**2
# print(bmi)


#
# make_pie(4)
"""

#TODO You are going to create a list called result which contains the numbers that are common in both files.

"""
#Add all file 1 numbers to list



with open("file1.txt", mode="r" ) as file1:
    data_file1 = file1.readlines()
    file1_list = [int(string.strip()) for string in data_file1]
    print(file1_list)

with open("file2.txt", mode="r") as file2:
    data_file2 = file2.readlines()
    file2_list = [int(string.strip()) for string in data_file2]

result = [num for num in file1_list if num in  file2_list]

print(result)
#[3, 6, 5, 33, 12, 7, 42, 13]
    # print(file1_list)

# result  = [number for number in #list and list2 if number in ]
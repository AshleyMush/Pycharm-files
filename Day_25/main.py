# # data = []
# # with open("weather_data.csv", mode="r") as weather_data:
# #     weather_data_contents = weather_data.read()
# #     data.append(weather_data_contents)
# # print(data)
#
# # import csv
# #
# #
# # temp = []
# # with open("weather_data.csv", mode="r") as weather_data:
# #     data = csv.reader(weather_data)
# #
# #     print(data)
# #
# #     for row in data:
# #         if row[1] != "temp":
# #             temp.append(row[1])
# #
# #     print(temp)
# #
# #     #TODO create list temp takes all temps as ints and put them in
#
# import pandas
# from  statistics import mean
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data)) #This is the collection of rows and colums
# print(type(data["temp"])) #A series is a list of data
# #
# # data_dict = data.to_dict()
# # TODO CONVERTING DATA TO DICT
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# #
# # #TODO cal Ave temp [Average]- adding a group of numbers and then dividing by the count of those numbers
# # #❤ AVERAGE = MEAN
# #
# # # Simple way to cal ave 👇
# # # count = len(temp_list)
# # #
# # # sum_temp = sum(temp_list)
# # #
# # # average = sum_temp/count
# # #
# # # print(round(average))
# #
# # average_temp = data["temp"].mean()
# # #most_common_temp
# # mode_temperate = data["temp"].mode()
# #
# # middle_temp = data["temp"].median()
# #
# # maximum_temp = data["temp"].max()
# #
# # print(round(average_temp))
# #
# # print(mode_temperate)
# #
# # print(round(middle_temp))
# #
# # print(f"This is the maximum temp {maximum_temp}")
# #
# # print(data.condition)
# #
# # #Getting hold of the data in a row using key
# #
# # print(data[data.day == "Monday"])
# # #Getting hold of the row with the highest temp
# # #    data[from data.temp == get hold of this func
# # print(data[data.temp == data.temp.max()])
#
# #Getting hold of Monday row
#
# # monday = data[data.day == "Monday"]
# # #            this is a row in our data set
# # print(monday.condition)
# #
# # #TODO Convert temperatures to ferenheight
# #
# # #f=c*1.8+32
# # #index.item() Return the first element of the underlying data as a Python scalar.
# # monday_celcius =  monday.temp.item()
# #
# # fahremheight = monday_celcius * 1.8 + 32
# #
# # print(int(fahremheight))
#
# #TODO CREATING A DATA FRAME FROM DATA WE SCRAPED
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
#
# }
#
# data = pandas.DataFrame(data_dict)
#
# print(data)
#
# #TODO Creating a CSV file from data frame
#
# data.to_csv("new_data.csv")


import pandas as pd

data = pd.read_csv("weather_data.csv")

# print(data)
#
# print(data.temp)
#
# data_dict = data.to_dict()
#
# print(data_dict)
# #CONVERTING SERIES TO LIST
# temp_list = data.temp.to_list()
#
# print(temp_list)
#Converting Mondays temp to farenheight
#TODO Getting a hold of a specific row items
monday = data[data.day == "Monday"]

print(monday)

# #f=c*1.8+32

monday_temp_C = monday.temp

print(monday_temp_C)

monday_F  = monday_temp_C *1.8+32

print(monday_F)


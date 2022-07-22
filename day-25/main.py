# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempratures = []
#     for row in data:
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))
#     print(tempratures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data.condition)

#get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

#Create a data from
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76,56,65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")


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
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_sqiurrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_sqiurrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sqiurrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_sqiurrels_count)
print(red_sqiurrels_count)
print(black_sqiurrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_sqiurrels_count, red_sqiurrels_count, black_sqiurrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")



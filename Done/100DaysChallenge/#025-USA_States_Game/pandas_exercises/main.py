import pandas as pd

# data = pandas.read_csv('./weather_data.csv')

# # data_dict = data.to_dict()
# # print(data_dict)
# # temp_dict = data['temp'].to_list()

# # print(data['temp'].max())

# print(data[data.temp == data.temp.max()])
# monday = (data[data.day == 'Monday'])
# monday["temp"] = monday["temp"] * 1.8 + 32
# print(monday)

data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrell_dict = {}
colors = data["Primary Fur Color"].unique()
squirrell_dict["Fur Color"] = colors[1:]
squirrell_dict["Count"] = []
 
for color in colors[1:]:
    squirrell_dict["Count"].append((data["Primary Fur Color"] == color).sum())
print(squirrell_dict)
df = pd.DataFrame(squirrell_dict)
df.to_csv('colors.csv')
import pandas

data = pandas.read_csv("Base/Projects/Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240327.csv")

# Initialize counts for each fur color
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

# Create dictionary for squirrel data
squi_data = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Number of Squirrels": [gray, black, cinnamon]
}

# Create DataFrame from dictionary
data = pandas.DataFrame(squi_data)

print(data)

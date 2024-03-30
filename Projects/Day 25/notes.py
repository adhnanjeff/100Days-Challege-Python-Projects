#Without using Pandas
""" import csv

with open("Base/Projects/Day 25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    
    print(temperature) """

#Using Pandas
import pandas

#data = pandas.read_csv("Base/Projects/Day 25/weather_data.csv")
#print(data.to_xml('example.xml'))

"Accessing values with their heading"
#print(data["temp"])
#print(len(data["temp"]))

"Using series"
#temp_list = data["temp"].to_list()
#print(sum(temp_list)/len(data["temp"]))

"Getting max and min temperature"
#print(data["temp"].min())
#print(data.temp.max())

#print(data["condition"])

"get data in rows"
#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#print(monday.condition)

#monday = data[data.day == "Monday"]
#temper = int(monday.temp)
#print(temper * 9/5 + 32)

"""Create a dataFrame"
data_dict = {
    "student": ["Shruthi","Adhnan", "Nethra"],
    "score": [90,87,85]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv") """


datasert = {
    'cars' : ["sedan", "volvo", "xuv","wagon"],
    'passsing' : [3,9,7,7]
}

myvar = pandas.DataFrame(datasert)
cars = myvar.cars

print(len(myvar[myvar.passsing == myvar.passsing]))


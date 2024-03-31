"This notes is for dictionary comprehension"

#Dictionary Comprehension
# new__dict = {new_key:new_value for item in list}
# new__dict = {new_key:new_value for (key,value) in dict.items()}
# new__dict = {new_key:new_value for (key,value) in dict.items() if test}
"""
import random
names = ["Shruthi", "Adhnan", "Nethra","Jeff","Vijay"]

new_dict = {item:random.randint(50,100) for item in names}

passed_students = {key:value for (key,value) in new_dict.items() if  value >= 70}
print(passed_students)
"""

#Auditorium 30
"""
sentence = input()
list1 = [char for char in sentence.split(" ")]
result = {item:len(item) for item in list1}
print(result)
"""

#Auditorium 31
"""
weather_c = eval(input())
weather_f = {key:(value * 9 / 5) + 32 for (key,value) in weather_c.items()}
print(weather_f)
"""

import pandas
student_dict = {
    "students":["Adhnan", "Shruthi", "Nethra"],
    "scores":[90,87,85]
}

data = pandas.DataFrame(student_dict)
#print(data) 
""" Without using pandas built in method
for (key, value) in data.items():
    print(value)
 """

#Without using pandas built in method
for (index, row) in data.iterrows():
    #print(row)
    #print(index)
    #print(row.students)
    if row.students == "Adhnan":
        print(row.scores)
 
"   {new_key:new_value for (index, row) in df.iterrows()}    "
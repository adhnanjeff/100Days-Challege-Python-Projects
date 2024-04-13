""" Without list comprehension

numbers = [1,2,3]
new_list = []

for num in numbers:
    add_1 = num + 3
    new_list.append(add_1)

print(new_list)

"""

"""
#With list comprehension

numbers = [1,2,3]
new_list = [ num + 3  for num in numbers ]
#new_list = [new_item for item in list] 
'Syntax🔼'

print(new_list)
"""

"""
name = "Adhnan"
letter_list = [letter for letter in name]
print(letter_list)
"""

"""
num_list = [numb*2 for numb in range(1,5)]
print(num_list)
"""

"""
names = ["Shruthi", "Adhnan", "Nethra","Jeff","Vijay"]
#new_name = [name for name in names if len(name) >= 6]
new_name = [name.upper() for name in names if len(name) < 6]
print(new_name)
"""

#Auditorium 28
"""
numbers = [1,1,2,3,5,8,13,21,34,55]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)
"""

#Auditorium 29
"""
numbers = [9,0,32,8,2,8,64,29,99]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
"""

#Auditorium 30
"""
with open("Base/Projects/Day 26/file1.txt") as f1:
    list1 = f1.readlines()
with open("Base/Projects/Day 26/file2.txt") as f2:
    list2 = f2.readlines()
    
result = [int(num) for num in list1 if num in list2]
print(result)
"""



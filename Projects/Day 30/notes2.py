height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / (height ** 2)

#Auditorium 33
fruits = eval(input())
# 🚨 Do not change the code above

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try: 
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit Pie")

# 🚨 Do not change the code below
make_pie(4)

#Auditorium 34
facebook_posts = eval(input())

total_likes = 0
# Catching the KeyError exception in the dictionary
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError as e:
        pass


print(total_likes)
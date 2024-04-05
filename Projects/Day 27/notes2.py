"Arguements"

"""
#Limited Arguements
def add(a, b):
    return a+b

ans = add(10,15)
print(ans)
"""

#Unlimited Arguements
"*args -> Arguements"
def add(*args): #It is taken in the form of tuples
    sum = 0
    for n in args:
        sum += n
    return sum

add1 = add(1,2,3,4,5,6,7,8,9,10)
#print(add1)


"Use of **kwargs arguements"

"*kwargs -> Keyword Arguements"
def calculate(n, **kwargs): #It is taken in the form of dictionaries
    #print(kwargs)
    #for key, value in kwargs.items():
    #    print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n) 

        #key = value
calculate(2, add = 3, multiply = 5)


class Cars:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
#If one of the keys is not givem it will throw an error
#The get() method can be used if we dont mention one of the key
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Cars(make="Nissan" ,model="GTR")
print(my_car.model)
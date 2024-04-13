"File not found error"
#with open("a_file.txt") as file:
#    file.read()

"Key Error"
#a_dictionary = {"key":"value"}
#value = a_dictionary["non_existent_key"]

"Index Error"
#fruit_list = ["Apple", "Orange", "Banana"]
#fruit = fruit_list[3]

"Type Error"
#text = "abc"
#print(text + 5)


#Example for Try and Catch block
try:
    file = open("my_file.xt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["ABCD"])

except FileNotFoundError: #Executes when the try block fails
    file = open("Base/Projects/Day 30/my_file.xt", "a")
    file.write("This is a sample text due to FileNotFound exception")

except KeyError as Error:
    print(f"{Error} not found")

else: #Executes when the try block succeeds
    print("The file was opened successfully")


finally:  #This block of code will always run
    #file.close()
    #print("File was closed")
    raise KeyError("Error")


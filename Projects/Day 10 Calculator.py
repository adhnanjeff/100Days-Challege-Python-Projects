def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def floordiv(a,b):
    return a//b

def mod(a,b):
    return a%b

def pow(a,b):
    return a**b

opt = {"+":sum,
        "-":sub,
        "*":mult,
        "/":div,
        "//":floordiv,
        "%":mod,
        "**":pow,
}

def calculator():
    print(''' 
     _____________________
    |  _________________  |
    | | AJ           0. | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
    ''')
    num1 = float(input("Enter the first number: "))

    for i in opt:
        print(i)

    operation = input("Enter the operation to perform from above: ")
    num2 = float(input("Enter the second number: "))

    cont = True
    calculation_function = opt[operation]
    ans = calculation_function(num1, num2)

    print(f"{num1}{operation}{num2} = {ans}")

    choice = input('Do you want to use the answer for more calculation "Yes" or "No"?').lower().strip()

    while cont:
        if choice == "yes":
            inp1 = ans
            operation = input("Enter the operation to perform from above: ")
            num2 = float(input("Enter the second number: "))

            calculation_function = opt[operation]
            ans = calculation_function(inp1, num2)

            print(f"{inp1}{operation}{num2} = {ans}")

            choice = input('Do you want to use the answer for more calculation "Yes" or "No"? Type "New" if you want to start a new calculation').lower().strip()

            if choice == "no":
                cont = False
                calculator()
            
            
        elif choice == "no":
            cont = False
            calculator()

        else:
            print("Invalid Choice")

calculator()
print("Calculation Ended")

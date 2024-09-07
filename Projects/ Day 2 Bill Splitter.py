print("Hello, welcome to my Bill splitter")
count = int(input("Enter the number of people you want to split the bill: "))
bill = float(input("Enter the total bill amount: "))
tip_percentage = int(input("Enter the tip percentage (10, 12, 15, or 20 percent): "))

if tip_percentage in {10, 12, 15, 20}:
    tip_amount = bill * (tip_percentage / 100)
    total = bill + tip_amount
    each_person_should_pay = total / count
 
    print(f"Total bill amount including {tip_percentage}% tip: ${total:.2f}")
    print(f"Each person should pay: ${each_person_should_pay:.2f}")
else:
    print(f"No tip. Each person should pay: ${bill/count:.2f}")

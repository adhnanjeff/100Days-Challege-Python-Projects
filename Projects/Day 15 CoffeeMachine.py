print("Welcome to Jeff's Coffee shop")

Water = 300
Milk = 200
Coffee = 100
Money = 0
Ice = 100
need_Coffee = True

Quarters = 0.25
Dimes = 0.10
Nickels = 0.05
Pennies = 0.01
total = 0.0

menu = [
    {"name": "Espresso", "water": 50, "brew": 18, "price": 1.99},
    {"name": "Latte", "water": 150, "brew": 24, "milk": 150, "price": 2.99},
    {"name": "Cold Coffee", "brew": 18, "milk": 200, "ice": 2, "price": 3.99}
]

while need_Coffee:
    order = input(
        "What would you like to have? (Espresso/ Latte/ Cold Coffee)\nOr type 'report' to get the amount of ingredients left (or) Type 'menu' to know our Menu: "
    ).lower()

    if order == "report":
        print(f"Water: {Water}ml")
        print(f"Milk: {Milk}ml")
        print(f"Coffee: {Coffee}g")
        print(f"Money: ${Money}")

    elif order == "menu":
        for item in menu:
            print(f"{item['name']} - ${item['price']}")

    elif order in ["espresso", "latte", "cold coffee"]:
        print('Please insert coins.')
        noQuarters = float(input("How many Quarters?"))
        noDimes = float(input("How many Dimes?"))
        noNickels = float(input("How many Nickels?"))
        noPennies = float(input("How many Pennies?"))

        total = noQuarters * Quarters + noDimes * Dimes + noNickels * Nickels + noPennies * Pennies

        for item in menu:
            if order == item["name"].lower():
                if total >= item["price"]:
                    change = total - item["price"]
                    Money += item["price"]
                    Water -= item["water"]
                    if "milk" in item:
                        Milk -= item["milk"]
                    if "ice" in item:
                        Ice -= item["ice"]
                    Coffee -= item["brew"]
                    print(f"Enjoy your {order.capitalize()}, Here is your ${change:.2f} change, Have a great Day!")
                    need_Coffee = False
                else:
                    print("Insufficient Amount")

    else:
        print("Don't ask for something out of our Menu, you know we don't have that 💀.")

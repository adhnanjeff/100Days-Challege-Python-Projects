bidders = {}
Flag = True
print(''' 
    
           ⢠⣿⣿⣶
         ⣰⣿⣿⣿⡿⠁
        ⣼⣿⣿⣿⡟⢀⣼⣿⣶⣤⣀
       ⣼⣿⣿⣿⠟⢀⣾⣿⣿⣿⣿⣿⣷⣦⣄
      ⣾⣿⣿⣿⠏⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀
      ⠻⢿⡿⠃⠰⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⢠⣿⣷
            ⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣠⣿⣿⣿⡟
             ⢴⣦⣄⠙⠻⣿⣿⣿⣿⣿⣿⡿⠃⣰⣿⣿⣿⡟
             ⣠⣈⠙⠻⣶⠄⠉⠛⠿⣿⡿⠁⣼⣿⣿⣿⠟
             ⣼⣿⣿⡿       ⢀⣾⣿⣿⣿
            ⣾⣿⣿⡿        ⠛⢿⣿
           ⣾⣿⣿⡟
          ⢠⣿⣿⣿⠟
 
''')
print("Welcome to the secret auction program!\n")

choice = input("Are there bidders available?").lower()
highest_bidder = ""
highest_bid = 0

if choice == "yes":
    while Flag:
        bidder = input("Enter your name: ")
        bid = int(input("Enter the bid amount: "))
        bidders[bidder] = bid
        choice = input("Are there any other bidders? ").lower()
        if choice == "no":
            Flag = False
            break
else:
    print("No bidders, therefore no auction today")

for ko in bidders:
    if bidders[ko] > highest_bid:
        highest_bidder = ko
        highest_bid = bidders[ko]

print(f"The highest bid is by {highest_bidder} with a bid of {highest_bid}")

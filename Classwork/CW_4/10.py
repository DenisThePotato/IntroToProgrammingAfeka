userInput = 0
while userInput < 1 or userInput > 10:
    userInput = int(input("Choose a number from 1 to 10: "))
    if userInput < 1 or userInput > 10:
        print("Try again.")
row = 1
spaces = userInput - row
stars = row
while row <= userInput:
    while spaces > 0:   #printing spaces (times: user input - row number)
        print(" ", end="")
        spaces -= 1
    while stars > 0:   #printing *'s (times: row number)
        print("*", end="")
        stars -= 1
    print()
    row += 1
    spaces = userInput - row
    stars = row
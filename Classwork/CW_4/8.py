userInput = 0
while userInput < 1 or userInput > 10:
    userInput = int(input("Choose a number from 1 to 10: "))
    if userInput < 1 or userInput > 10:
        print("Try again.")
repetitions = 1
length = repetitions
while repetitions <= userInput:
    while length > 0:
        print("*", end="")
        length -= 1
    print()
    repetitions += 1
    length = repetitions
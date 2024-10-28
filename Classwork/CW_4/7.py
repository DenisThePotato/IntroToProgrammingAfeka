userInput = 0
while userInput < 1 or userInput > 10:
    userInput = int(input("Choose a number from 1 to 10: "))
    if userInput < 1 or userInput > 10:
        print("Try again.")
repetitions = userInput
rowsLeft = userInput
while rowsLeft > 0:
    while repetitions > 0:
        print("*", end="")
        repetitions -= 1
    print()
    repetitions = userInput
    rowsLeft -= 1
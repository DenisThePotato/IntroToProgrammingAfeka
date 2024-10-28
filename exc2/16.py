def sumOfDividers(num):   # Returns value of sum of dividers.
    sum = 0
    for i in range (1, (int(num / 2) + 1)):
        if num % i == 0:
            sum += i
    return sum

numbersNeeded = int(input("How many mates do you want to find? "))
currentNumber = 2
for i in range (numbersNeeded):
    isMate = False
    while not isMate:
        potentialMate = sumOfDividers(currentNumber)   # Sum of dividers of current number
        dividerSumDivider = sumOfDividers(potentialMate)   # Sum of dividers of potential mate
        if currentNumber == dividerSumDivider and potentialMate > currentNumber:
            isMate = True
            print(f"{currentNumber} and {potentialMate} are mates.")
        currentNumber += 1
# Question 9: Makes up a new number out of the first number's digits, times the second number's digits.
# parameter numOfNums- number which digits are used to form the new number.
# parameter numToUse- the number which digits represent times to use said digit.
# return the new number.
def nine(numOfNums, numToUse):
    multiplier = 1
    newNumber = 0
    for i in range(9):
        while numOfNums % 10 == 0:   # Using % 10 on a number returns its digit number.
            numToUse = int(numToUse / 10)   # Using / 10 on a number "removes" its digit number.
            numOfNums = int(numOfNums / 10)
        else:
            numOfNums -= 1
            newNumber += (numToUse % 10) * multiplier
            multiplier *= 10
    return newNumber

# Question 10: Reverses grouplets of given number and combines them to a number.
# parameter number- number to be manipulated.
# parameter digit- grouplet size.
# return final number after manipulation.
def ten(number = -1, digit = -1):
    # Using %(10**digits) gives us the last digits number of a given number.
    while number < 0:
        number = int(input("Please input a positive number: "))
    while digit < 1 or digit > 9:
        digit = int(input("Please input a positive digit: "))
    newNumber = 0
    power = 0
    while number != 0:
        digitlet = number % (10 ** digit)   # creates the digit-let, last digit numbers of input number.
        reversedDigitlet = 0
        for i in range(digit):   # creates the reversed triplet.
            reversedDigitlet += ((digitlet % 10) * (10 ** (digit - i - 1)))
            digitlet = int(digitlet / 10)
        newNumber += reversedDigitlet * (10**power)
        power += digit
        number = int(number / (10 ** digit))
    print(newNumber)

# Question 13: Prints a hourglass.
# parameter base- width of hourglass.
def thirteen(base = -1):
    while base < 1 or base % 2 == 0:
        base = int(input("How thicc do you like your triangles? "))
    for i in range(base, 0, -1):
        print(" " * (base - i), end="")
        print("* " * i)

    for i in range(2, base + 1):
        print(" " * (base - i), end="")
        print("* " * i)

# Question 15: Prints a tree.
# parameter base- width of tree.
def fifteen(base = -1):
    while base < 1 or base % 2 == 0:
        base = int(input("How thicc do you like your triangles? "))
    for i in range(base + 1):
        for i in range(1, base + 1):
            print(" " * (base - i), end="")
            print("* " * i)
    for i in range(base):
        print(" " * (base - 1) + "*")

# Question 16: Finds number mates, and prints them.
# parameter mates- number of mates to be searched for.
def sixteen(mates = 8):
    def sumOfDividers(num):  # Returns value of sum of dividers.
        sum = 0
        for i in range(1, (int(num / 2) + 1)):
            if num % i == 0:
                sum += i
        return sum
    mates = int(input("How many mates do you want to find? "))
    currentNumber = 2
    for i in range(mates):
        isMate = False
        while not isMate:
            potentialMate = sumOfDividers(currentNumber)  # Sum of dividers of current number
            dividerSumDivider = sumOfDividers(potentialMate)  # Sum of dividers of potential mate
            if currentNumber == dividerSumDivider and potentialMate > currentNumber:
                isMate = True
                print(f"{currentNumber} and {potentialMate} are mates.")
            currentNumber += 1

# Mind you- the functions that return specific things wont print.
# We were instructed for them to just be returned.
option = 0
while option != -1:
    print("------------------------------------------------------------")
    print("Pick your poison (input one number from the options below):")
    print("Generate a new number based on two numbers: 9")
    print("Generate a number based on reversing segments of it: 10")
    print("Print a hourglass: 13")
    print("Print a tree: 15")
    print("Find mate numbers: 16")
    print("exit: -1")
    print("------------------------------------------------------------")
    option = int(input("User's choice: "))
    if option == 9 or option == 10:
        var1 = 0
        var2 = 0
        var1, var2 = input("Enter two numbers here: ").split()
        var1 = int(var1)
        var2 = int(var2)
        if option == 9:
            nine(var1, var2)
        elif option == 10:
            ten(var1, var2)
    else:
        var = int(input("Enter a number: "))
        if option == 13:
            thirteen(var)
        if option == 15:
            fifteen(var)
        if option == 16:
            sixteen(var)
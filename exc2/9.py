# Using %10 on a number returns its digit number.
# Using /10 on a number "removes" its digit number.
numOfNums = int(input("insert the first number: "))
numToUse = int(input("insert the second number: "))
multiplier = 1
newNumber = 0
for i in range(9):
    while numOfNums % 10 == 0:
        numToUse = int(numToUse / 10)
        numOfNums = int(numOfNums / 10)
    else:
        numOfNums -= 1
        newNumber += (numToUse % 10) * multiplier
        multiplier *= 10
print(newNumber)
# Chapter 6- question 13: Prints array as a bar graph.
# parameter arr- array to be translated into graph.
def six_thirteen(arr):
    highestValue = 0
    for i in range(len(arr)):
        if int(arr[i]) > highestValue:
            highestValue = int(arr[i])
    for i in range(highestValue):
        for j in range(len(arr)):
            if int(arr[j]) >= (highestValue - i):
                print("* ", end="")
            else:
                print("  ", end="")
        print()
    for i in range(len(arr)):
        print("--", end="")
    print()
    for i in range(len(arr)):
        print(f"{arr[i]} ", end="")

# Chapter 6- question 14: Addition of numbers represented by arrays.
# parameter arr1- first array.
# parameter arr2- second array.
# return final array after addition.
def six_fourteen(arr1, arr2):
    index = 0
    multiplier = 1
    finalNumber = 0
    while index < len(arr1) or index < len(arr2):   # Get the combined number.
        if index < len(arr1):
            finalNumber += arr1[len(arr1) - 1 - index] * multiplier
        if index < len(arr2):
            finalNumber += arr2[len(arr2) - 1 - index] * multiplier
        index += 1
        multiplier *= 10
    finalList = []
    for i in  range(len(str(finalNumber))):
        finalList.insert(0, int(finalNumber % 10))
        finalNumber = int(finalNumber / 10)
    return finalList

# Chapter 6- question 16: Find out if a number is a Kaprekar number and return its parts via a list.
# parameter num- number to be checked.
# parameter arr- array for the parts of the Kaprekar number to be put in.
# return true if the number is indeed a Kaprekar number, otherwise, false.
def six_sixteen_fast(num, arr = [0, 0]):
    numInPower = num**2
    openingNumber = int(str(numInPower)[0:int(len(str(numInPower))/2)])
    closingNumber = int(str(numInPower)[int(len(str(numInPower))/2):])
    if openingNumber + closingNumber == num:
        arr[0] = openingNumber
        arr[1] = closingNumber
        return True
    return False
# Same functionality, just limited to numerical manipulations.
def six_sixteen_slow(num, arr = [0, 0]):
    numInPower = num ** 2
    closingNumber = 0
    multiplier = 1
    if int(len(str(numInPower))) % 2 == 0:
        times = int(len(str(numInPower))/2)
    else:
        times = int(len(str(numInPower))/2) + 1
    for i in range(times):
        closingNumber += numInPower%10 * multiplier
        numInPower = int(numInPower / 10)
        multiplier *= 10
    openingNumber = numInPower
    if openingNumber + closingNumber == num:
        arr[0] = openingNumber
        arr[1] = closingNumber
        return True
    return False

# Chapter 7: Question 3: Prints a matrix (snake pattern).
# parameter rows- number of rows in the matrix.
# parameter columns- number of columns in the matrix.
def seven_three(rows = 5, columns = 5):
    # The inner for loop represents the columns and the outer for represents the rows unlike other languages:
    # matrix[rows][columns].
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    currentValue = 1
    for c in range(columns):
        if c % 2 == 0:   # values go from the top of column to the bottom
            # matrix[top row->bottom row][current column]
            for r in range(rows):
                matrix[r][columns-1-c] = currentValue
                currentValue += 1
        else:   # values go from the bottom of column to the top
            # matrix[bottom row->top row][current column]
            for r in range(rows):
                matrix[rows-1-r][columns-1-c] = currentValue
                currentValue += 1
    for c in range(rows):
        for r in range(columns):
            print(f"{matrix[c][r]}     ", end="")
        print()

# Chapter 7- question 7: Find out if there's a way out of a matrix using '-' and '|'.
# parameter matrix- matrix with possible way out.
# return True if there's a way out, False if there isn't.
def seven_seven(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    curRow = 0
    curCol = columns - 1
    while curRow < rows and curCol < columns:
        if matrix[curRow][curCol] == 'a':
            break
        if matrix[curRow][curCol] == '-':
            curCol -= 1
        if matrix[curRow][curCol] == '|':
            curRow += 1
    if curRow >= rows:
        return True
    return False

# checks if the sum of digits of a number is equal to another number.
# param number- the number which supplies the sum of digits.
# param sumOfDigits- the number that represents the sum of digits.
# return True if it is the sum.
def nine_nineteen(number, sumOfDigits):
    if number == 0 and sumOfDigits == 0:
        return True
    if (number == 0 and sumOfDigits != 0) or sumOfDigits < 0:
        return False
    return nine_nineteen((int(number / 10)), (sumOfDigits - int(number % 10)))

# the mathematical sequence: 1, 2, 3, 6, 4, 13, 7, 24, 11, 42...
# the indices 1, 2 and 3 are 1, 2 and 3, respectively.
# every 2n index, n >= 2: A(2n) = A(2n-1) + A(2n-2) + A(2n-3)
# every 2n+1 index, n>=2: A(2n+1) = |A(n-1) - A(n-2)|
# param index- gives the index of number to be searched for in the sequence.
# return the number in place index.
def nine_twenty(index):
    if index == 3:
        return 3
    elif index == 2:
        return 2
    elif index == 1:
        return 1
    elif index % 2 == 0:
        return (nine_twenty(index-1) + nine_twenty(index-2) + nine_twenty(index-3))
    elif index % 2 != 0:
        return abs(nine_twenty(index-1)-nine_twenty(index-3))

# calculates how many possibilities there are to climb on a ladder, taking 1 or two stages at a time.
# param stages- number of ladder stages
# return number of possibilities.
def nine_twenty_one(stages):
    if stages == 1:
        return 1
    elif stages == 2:
        return 2
    else:   # whether the first step is one stage, or two.
        return(nine_twenty_one(stages-1) + nine_twenty_one(stages-2))

# I did question number 21 instead of 22, i didn't understand the question... and there wasn't a question 23.
chapter = -1
question = -1
while chapter != 0 and question != 0:
    print("------------------------------------------------------------")
    print("Pick your poison (input one number from the options below):")
    print("Chapter 6 question 13: 6 13")
    print("Chapter 6 question 14: 6 14")
    print("Chapter 6 question 16: 6 16")
    print("Chapter 7 question 3: 7 3")
    print("Chapter 7 question 7: 7 7")
    print("Chapter 9 question 19: 9 19")
    print("Chapter 9 question 20: 9 20")
    print("Chapter 9 question 21: 9 21")
    print("exit: 0 0")
    print("------------------------------------------------------------")
    chapter, question = input("User's choice: ").split()
    chapter = int(chapter)
    question = int(question)
    if chapter == 6:
        if question == 13:
            columns = int(input("how many columns?"))
            array = [0] * columns
            for i in range(columns):
                array[i] = int(input(f" the {i + 1} index: "))
            six_thirteen(array)

        if question == 14:
            firstArrIndexes = int(input("how many indexes for the first array?"))
            arr1 = [0] * firstArrIndexes
            for i in range(firstArrIndexes):
                arr1[i] = int(input(f" the {i + 1} index: "))
            secondArrIndexes = int(input("how many indexes for the second array?"))
            arr2 = [0] * secondArrIndexes
            for i in range(secondArrIndexes):
                arr2[i] = int(input(f" the {i + 1} index: "))
            print(six_fourteen(arr1, arr2))
        if question == 16:
            potentialKaprekar = int(input("what number do you want checked? "))
            if int(input("do you want to wait extra time for absolutely no reason? 0/1")) == 1:
                print(six_sixteen_slow(potentialKaprekar))
            else:
                print(six_sixteen_fast(potentialKaprekar))
    if chapter == 7:
        if question == 3:
            rows = int(input("how many rows?"))
            columns = int(input("how many rows?"))
            seven_three(rows, columns)
        if question == 7:
            first = [['a', 'a', 'a', 'a', 'a', '|'],
                     ['a', 'a', 'a', 'a', 'a', '|'],
                     ['a', 'a', 'a', '|', '-', '-'],
                     ['a', 'a', '|', '-', 'a', 'a'],
                     ['a', '|', '-', 'a', 'a', '|']]
            second = [['a', 'a', 'a', 'a', 'a', '|'],
                      ['a', 'a', 'a', 'a', 'a', '|'],
                      ['a', 'a', 'a', '|', '-', '-'],
                      ['a', 'a', '|', '-', 'a', 'a'],
                      ['a', 'a', '|', 'a', 'a', '|']]
            third = [['a', 'a', 'a', 'a', 'a', '|'],
                     ['a', 'a', 'a', 'a', 'a', '|'],
                     ['a', 'a', 'a', '|', '-', '-'],
                     ['a', 'a', '|', '-', 'a', 'a'],
                     ['a', 'a', '-', 'a', 'a', '|']]
            fourth = [['a', 'a', 'a', 'a', 'a', '|'],
                      ['a', 'a', 'a', 'a', 'a', '|'],
                      ['a', 'a', 'a', '|', '-', '|'],
                      ['a', 'a', '|', '-', 'a', 'a'],
                      ['a', '|', '-', 'a', 'a', '|']]
            matrixToUse = int(input("pick a number from 1 to 4 (each correlates to a different matrix)"))
            if matrixToUse == 1:
                print(seven_seven(first))
            elif matrixToUse == 2:
                print(seven_seven(second))
            elif matrixToUse == 3:
                print(seven_seven(third))
            else:
                print(seven_seven(fourth))
    if chapter == 9:
        if question == 19:
            number = int(input("pick a number: "))
            sumOfDigits = int(input("pick a potential sum of digits: "))
            nine_nineteen(number, sumOfDigits)
        if question == 20:
            index = int(input("what index do you want to be found?"))
            nine_twenty(index)
        if question == 22:
            stages = int(input("high tall is the ladder? "))
            nine_twenty_one(stages)
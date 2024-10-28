# q1 has dictionaries.
import math

# find the closest number in value to a given index in a list, and return its value.
def q2(list, index):
    number = list[index]
    difference = abs(number - list[0])
    neighbourIndex = -1
    for i in range(1, len(list)):
        if i == index:
            continue
        if abs(number - list[i]) < difference:
            neighbourIndex = i
            difference = abs(number- list[i])
    return neighbourIndex

# calculate the average of the values in a given list.
def q3_a(list):
    if len(list) == 0:
        return 0
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return (sum / len(list))

# my personal understanding of the theorem.
def q3_b_myVersion(list):
    totalSum = 0
    for i in range(len(list)):
        tempSum = 0
        for j in range(len(list)):
            if j != i:
                tempSum += list[j]
        totalSum += (list[i] - tempSum)**2
    return math.sqrt(totalSum/len(list))

# calculated with x(top hat) being the average.
# calculate the standard deviation.
def q3_b_theirVersion(list):
    average = q3_a(list)
    if len(list) == 0:
        return 0
    totalSum = 0
    for i in range(len(list)):
        totalSum += ((list[i]-average)**2)
    return math.sqrt(totalSum / len(list))

# gets a binary number and calculates its value.
# 0  = 0, 1 = 1.
# 01 = 3, 10 = 4, 11 = 5.
# every index represents 2**index.
def q4_string(binary, assist = 0):
    if len(str(binary)) == 1:
        return int(binary) * (2**assist)
    binaryString = str(binary)
    return ((int(binaryString[0]) * 2**assist) + q4(binaryString[1:len(binaryString)], (assist + 1)))

# 2**digits, pass without digits and higher power
def q4_int(binary, assist = 0):
    if binary == 1:
        return (2**assist)
    return (((binary % 10) * 2**assist) + q4_int((binary // 10), (assist + 1)))






# q2 tests   ---WORKS
print("q2- ", end="")
print(q2([3,5,2,18,9,4], 3))

# q3_a tests   ---WORKS
print("q3_a- ", end="")
print(q3_a([3,5,2,18,9,4]))

# q3_b_myVersion tests
print("q2_b_mine- ", end="")
print(q3_b_myVersion([3,5,2,18,9,4]))

# q3_b_theirVersion tests   ---WORKS
print("q3_b_their- ", end="")
print(q3_b_theirVersion([3,5,2,18,9,4]))

# q4 tests   ---WORKS
print(q4_int(101))
print(q4_int(1001))
print(q4_int(111001))

# tests

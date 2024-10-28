# Using %(10**digits) gives us the last digits number of a given number.
number = -1
digit = -1

while number < 0:
    number = int(input("Please input a positive number: "))

while digit < 1 or digit > 9:
    digit = int(input("Please input a positive digit: "))

newNumber = 0
power = 0

while number != 0:
    digitlet = number % (10 ** digit)   # creates the digit-let, last digit numbers of input number.
    reversedDigitlet = 0
    for i in range(digit):   # creates the reversed triplet - there is a problem when triplet not digit nums
        reversedDigitlet += ((digitlet % 10) * (10 ** (digit - i - 1)))
        digitlet = int(digitlet / 10)
    newNumber += reversedDigitlet * (10**power)
    power += digit
    number = int(number / (10 ** digit))

print(newNumber)
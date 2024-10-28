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

print(nine_nineteen(4362, 15))

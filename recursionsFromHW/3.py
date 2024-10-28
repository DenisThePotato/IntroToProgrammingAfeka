# returns true if all digits are even, and if not, false.
def areAllDigitsEven(number):
    if number == 0:
        return True
    if (number % 10) % 2 == 0:
        return areAllDigitsEven(number // 10)
    else:
        return False

print(areAllDigitsEven(0))
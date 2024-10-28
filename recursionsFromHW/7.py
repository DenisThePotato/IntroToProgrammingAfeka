def isDigitInNumber(number, digit):
    if number == 0:
        return False
    if number % 10 == digit:
        return True
    return isDigitInNumber((number // 10), digit)

print(isDigitInNumber(63423455, 0))
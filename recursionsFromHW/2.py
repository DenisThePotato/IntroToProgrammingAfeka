# param number number to be checked.
# return number of even digits in number.
def numberOfEven(number):
    if number == 0:
        return 0
    if (number % 10) % 2 == 0:
        return (1 + numberOfEven(number // 10))
    else:
        return numberOfEven(number // 10)

print(numberOfEven(22566098))
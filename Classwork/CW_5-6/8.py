def factorialRecursive(number):
    if number == 1:
        return number
    return number * factorial(number - 1)

def factorialIterative(number):
    result = 1
    for i in range (number):
        result *= (i + 1)
    return result

print(factorialIterative(5))
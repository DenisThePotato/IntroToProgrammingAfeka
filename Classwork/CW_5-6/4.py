def power(base, power):
    result = 1
    for i in range(power):
        result *= base
    return result

print(power(5, 3))
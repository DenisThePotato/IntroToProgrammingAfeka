def fibonacci(index):
    if index == 1:
        return 1
    next = 1
    current = 1
    for i in range (index):
        temp = current
        current = next
        next = (next + temp)
    return current

print(fibonacci(5))
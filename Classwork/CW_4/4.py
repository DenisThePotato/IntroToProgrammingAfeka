sum = 0
number = 0
while True:
    number = int(input("Input a number (0 to exit): "))
    if number == 0:
        break
    sum += number
print(sum)

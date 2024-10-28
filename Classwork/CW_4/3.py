number = int(input("your number: "))
sum = 0
while number != 0:
    if (number % 10) % 2 == 0:
        sum += number % 10
    number = int(number / 10)
print (f"sum of even digits: {sum}")
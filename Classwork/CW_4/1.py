#calculate number of digits in number
number = int(input("your number: "))
digits = 0
while number != 0:
    number = int(number / 10)
    digits += 1
print (f"The number has {digits} digits")

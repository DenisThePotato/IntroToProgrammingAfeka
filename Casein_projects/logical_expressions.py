int1 = int(input("First int: "))
int2 = int(input("First int: "))
if int1 % 2 == 0 and int2 % 2 == 0:
    print("Both numbers are even.")
elif int1 % 2 != 0 and int2 % 2 != 0:
    print("Both numbers are odd.")
else:
    print("One number is even, and the other is odd.")
# A(n) = A(n-1) + A(n-2)
# A(1) = 0
# A(2) = 1
# A = 0, 1, 1, 2, 3, 5, 8
number = int(input("your fib num: "))
oneBeforeIndex = 0
index = 1
oneAfterIndex = 2
while index < number:
    temp = oneAfterIndex
    oneAfterIndex = oneAfterIndex + index
    oneBeforeIndex = index
    index = temp
if index == number or number == 0:
    print("yes")
else:
    print("no")

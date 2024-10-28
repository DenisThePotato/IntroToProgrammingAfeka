# A top number is a number which is built from rising numbers- top number- lowering numbers
# For example:
# 123454321
# 134541
number = input("input a number: ")
topIndex = 0
isTopNumber = True
for i in number[:]: # Find the highest number
    if int(number[i]) < int(number[i+1]):
        continue
    else:
        topIndex = i
        break
for i in number[topIndex:len(number)-2]:
    if int(number[i]) > int(number[i+1]):
        continue
    else:
        isTopNumber = False
if isTopNumber:
    print("the number is a top number.")
else:
    print("the number is not a top number.")
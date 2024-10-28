#Q1
char = input("input the character you want repeated: ")
for count in range(4):
 print(char)

#Q2
char = input("input the character you want repeated: ")
for count in range(5):
 print(char + " ", end="")

#Q3
name = input("What's your name? ")
surname = input("What's your surname? ")
print(f"firstname : {name}, lastname : {surname}")

#Q4
length = int(input("What is your desired length? "))
width = int(input("What is your desired width? "))
temp = length
length = width
width = temp
print(f"length = {length}, width = {width}")


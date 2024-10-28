base = -1
while base < 1 or base % 2 == 0:
    base = int(input("How thicc do you like your triangles? "))
for i in range(base, 0, -1):
    print(" " * (base - i), end="")
    print("* " * i)

for i in range(2, base + 1):
    print(" " * (base - i), end="")
    print("* " * i)


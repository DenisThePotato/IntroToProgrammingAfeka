first= int(input("choose starting number: "))
second = int(input("choose end number: "))
if first >= second:
    print("wrong input")
else:
    for i in range (first, second+1):
        if i % 2 == 0:
            continue
        elif i == second:
            print(f"{i}")
        else:
            print(f"{i},", end="")
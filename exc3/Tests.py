array = [[3, 2, 3], [4, 5, 6], [7, 3, 9]]
dood = 1
for i in range(3):
    for j in range(3):
        if array[i][j] == 3 and dood == 1:
            dood += 1
            print("continuing")
            break
        elif array[i][j] == 3:
            print("found the 3")
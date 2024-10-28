# Go over list, find highest value
# if highest value - counter  > index in array, then print a *
def printGraph(arr):
    highestValue = 0
    for i in range(len(arr)):
        if int(arr[i]) > highestValue:
            highestValue = int(arr[i])
    for i in range (highestValue):
        for j in range(len(arr)):
            if int(arr[j]) >= (highestValue - i):
                print("* ", end="")
            else:
                print("  ", end="")
        print()
    for i in range(len(arr)):
        print("--", end="")
    print()
    for i in range(len(arr)):
        print(f"{arr[i]} ", end="")

array = [9, 4, 5, 6, 8]
printGraph(array)
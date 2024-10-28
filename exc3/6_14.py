def six_fourteen(arr1, arr2):
    index = 0
    multiplier = 1
    finalNumber = 0
    while index < len(arr1) or index < len(arr2):   # Get the combined number.
        if index < len(arr1):
            finalNumber += arr1[len(arr1) - 1 - index] * multiplier
        if index < len(arr2):
            finalNumber += arr2[len(arr2) - 1 - index] * multiplier
        index += 1
        multiplier *= 10
        print(finalNumber)
    finalList = []
    for i in  range(len(str(finalNumber))):
        finalList.insert(0, int(finalNumber % 10))
        finalNumber = int(finalNumber / 10)
        print(finalList)
    return finalList
# tests
firstArr = [1, 2, 3, 6]
secodnArr = [1, 2, 3, 4]
print(numberMerger(firstArr, secodnArr))
# inverts a list's values.
def switchValues(list, startIndex, endIndex):
    if startIndex == endIndex or startIndex > endIndex:
        return list
    temp = list[startIndex]
    list[startIndex] = list[endIndex]
    list[endIndex] = temp
    return switchValues(list, startIndex + 1, endIndex - 1)

list = [1, 2, 3, 4, 5, 6]
print(list)
switchValues(list, 0, 5)
print(list)
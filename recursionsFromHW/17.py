def bNumbersInRowUntil(list, digit):
    if digit == 0:
        return True
    if len(list) == 0:
        return False
    if list[len(list) - 1] == digit:
        return bNumbersInRowUntil(list[:len(list)-1], digit - 1)
    else:
        return bNumbersInRowUntil()

def recursiveSeriesFinder(list, digit):
    if len(list) < digit - 1:
        return False
    if list[0] == 1:
        indexValue = 1
        for i in range(digit):
            if list[i] == indexValue:
                indexValue += 1
            else:
                return recursiveSeriesFinder(list[1:], digit)
        return True
    return recursiveSeriesFinder(list[1:], digit)

print(recursiveSeriesFinder([1,0,3,4,0,3,1,2,3,4], 4))

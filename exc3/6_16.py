# create the two functions they wanted: "do you want to wait extra time for absolutely no reason?"
def six_sixteen_fast(num, arr = [0, 0]):
    numInPower = num**2
    openingNumber = int(str(numInPower)[0:int(len(str(numInPower))/2)])
    closingNumber = int(str(numInPower)[int(len(str(numInPower))/2):])
    if openingNumber + closingNumber == num:
        arr[0] = openingNumber
        arr[1] = closingNumber
        return True
    return False

def six_sixteen_slow(num, arr = [0, 0]):
    numInPower = num ** 2
    closingNumber = 0
    multiplier = 1
    if int(len(str(numInPower))) % 2 == 0:
        times = int(len(str(numInPower))/2)
    else:
        times = int(len(str(numInPower))/2) + 1
    for i in range(times):
        closingNumber += numInPower%10 * multiplier
        numInPower = int(numInPower / 10)
        multiplier *= 10
    openingNumber = numInPower
    if openingNumber + closingNumber == num:
        arr[0] = openingNumber
        arr[1] = closingNumber
        return True
    return False

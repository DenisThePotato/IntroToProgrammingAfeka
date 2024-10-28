def isOnePairSwitchable(number):
    if number < 10:
        return False
    if ((number % 10) % 2) != ((number // 10) % 2):
        return True
    else:
        return isOnePairSwitchable(number // 10)

print(isOnePairSwitchable(333333))

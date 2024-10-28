# return true if every next digit of number has a different evenness.
def isSwitchable(number):
    if number < 10:
        return True
    if ((number % 10) % 2) != ((number // 10) % 2):
        return isSwitchable(number // 10)
    else:
        return False

print(isSwitchable(567872))
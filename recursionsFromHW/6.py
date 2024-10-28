def bAllLettersCapital(string, length):
    if length == 0:
        return True
    if string[length - 1] == string[length - 1].capitalize():
        return bAllLettersCapital(string, length - 1)
    return False

print(bAllLettersCapital("SdKRSHSJR", 9))
def bOnlySameCapitalization(list, length):
    if length == 0:
        return True
    if (list[0] == list[0].capitalize()) == (list[len(list) - length] == list[len(list) - length].capitalize()):
        return bOnlySameCapitalization(list, length - 1)
    return False

print(bOnlySameCapitalization(['B', 'C', 'B', 'D'], 4))
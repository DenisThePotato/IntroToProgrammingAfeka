# param list a list
# return True if all numbers are even, False if not.
def areAllListMembersEven(list, length):
    if length == 0:
        return True
    if list[len(list)-length] % 2 == 0:
        return areAllListMembersEven(list, length - 1)
    return False

print(areAllListMembersEven([-2, 4, 6, 8, 12, 5], 6))
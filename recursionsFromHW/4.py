# param list a list we get
# return number of even numbers in list.
def evenNumberInList(list, length):
    print(f"current len: {length}")
    if length == 0:
        return 0
    if list[len(list)-length] % 2 == 0:
        return 1 + evenNumberInList(list, length - 1)
    return evenNumberInList(list, length - 1)

print(evenNumberInList([1, 2, 2, 5, 0], 5))
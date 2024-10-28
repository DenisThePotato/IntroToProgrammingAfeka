# both are organized in an ascending manner: [1,2,3]
# every time one of the two lists goes into C
def merge_lists(listA, lenA, listB, lenB, c):
    if lenA > 0 and lenB > 0:
        if listA[lenA - 1] > listB[lenB - 1]:
            c[lenA + lenB - 2] = listA[lenA - 1]
            return merge_lists(listA, (lenA-1), listB, lenB, c)
        else:
            c[lenA + lenB - 2] = listB[lenB - 1]
            return merge_lists(listA, lenA, listB, (lenB-1), c)
    elif lenA > 0:
        c[lenA - 1] = listA[lenA - 1]
        return merge_lists(listA, (lenA - 1), listB, lenB, c)
    elif lenB > 0:
        c[lenB - 1] = listA[lenB - 1]
        return merge_lists(listA, lenA, listB, (lenB - 1), c)
    else:
        return

a = [1, 3, 5]
b = [2, 4, 6]
c = [0, 0, 0, 0, 0, 0]
merge_lists(a, len(a), b, len(b), c)
print(a)
print(b)
print(c)

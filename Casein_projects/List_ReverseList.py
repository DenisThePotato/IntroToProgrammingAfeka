def reverse_list(lst: [str]):
    list = []
    for i in range((len(lst)-1), -1, -1):
        list.append(lst[i])
    lst = list
    return lst
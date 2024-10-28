def get_max_min_list(lst):
    if len(lst) == 0:
        return [0, 0]
    max = lst[0]
    min = lst[0]
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
        if lst[i] < min:
            min = lst[i]
    return [max, min]
def calculate_average(lst):
    if len(lst) == 0:
        return 0
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return (sum / len(lst))
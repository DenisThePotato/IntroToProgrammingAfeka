# q1: given a string, check if the first half is the same as the second half. do so recursively.
# [a, b, c, a, b] - True.
# [a, b, a, b] - True.
def subStringInList(list, subString):
    timesAppeared = 0
    for i in range(len(list)):
        indexFound = 0
        while list[i][indexFound:].find(subString) != -1 and indexFound < len(list[i]):
            indexFound = list[i][indexFound:].find(subString) + 1
            timesAppeared += 1
    return timesAppeared

#print(subStringInList(["abcab","ababgab"], "ab"))
print(99 % 0)
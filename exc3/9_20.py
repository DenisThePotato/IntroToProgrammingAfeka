# the mathematical sequence: 1, 2, 3, 6, 4, 13, 7, 24, 11, 42...
# every 2n index, n >= 2: A(2n) = A(2n-1) + A(2n-2) + A(2n-3)
# every 2n+1 index, n>=2: A(2n+1) = |A(n-1) - A(n-2)|
# param index- gives the index of number to be searched for in the sequence.
# return the number in place index.
def nine_twenty(index):
    if index == 3:
        return 3
    elif index == 2:
        return 2
    elif index == 1:
        return 1
    elif index % 2 == 0:
        return (nine_twenty(index-1) + nine_twenty(index-2) + nine_twenty(index-3))
    elif index % 2 != 0:
        return abs(nine_twenty(index-1)-nine_twenty(index-3))

print(nine_twenty(7))
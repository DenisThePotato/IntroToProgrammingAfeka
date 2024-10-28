def seven_seven(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    curRow = 0
    curCol = columns - 1
    while curRow < rows and curCol < columns:
        if matrix[curRow][curCol] == 'a':
            break
        if matrix[curRow][curCol] == '-':
            curCol -= 1
        if matrix[curRow][curCol] == '|':
            curRow += 1
    if curRow >= rows:
        return True
    return False

print('first two should be true, the last two false.')
first = [['a', 'a', 'a', 'a', 'a', '|'],
          ['a', 'a', 'a', 'a', 'a', '|'],
          ['a', 'a', 'a', '|', '-', '-'],
          ['a', 'a', '|', '-', 'a', 'a'],
          ['a', '|', '-', 'a', 'a', '|']]
print(seven_seven(yep1))
second = [['a', 'a', 'a', 'a', 'a', '|'],
          ['a', 'a', 'a', 'a', 'a', '|'],
          ['a', 'a', 'a', '|', '-', '-'],
          ['a', 'a', '|', '-', 'a', 'a'],
          ['a', 'a', '|', 'a', 'a', '|']]
print(seven_seven(yep2))
third = [['a', 'a', 'a', 'a', 'a', '|'],
          ['a', 'a', 'a', 'a', 'a', '|'],
          ['a', 'a', 'a', '|', '-', '-'],
          ['a', 'a', '|', '-', 'a', 'a'],
          ['a', 'a', '-', 'a', 'a', '|']]
print(seven_seven(nope1))
fourth = [['a', 'a', 'a', 'a', 'a', '|'],
          ['a', 'a', 'a', 'a', 'a', '|'],
          ['a', 'a', 'a', '|', '-', '|'],
          ['a', 'a', '|', '-', 'a', 'a'],
          ['a', '|', '-', 'a', 'a', '|']]
print(seven_seven(nope2))
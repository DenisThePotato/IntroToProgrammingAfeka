def seven_three(rows = 5, columns = 5):
    # The inner for loop represents the columns and the outer for represents the rows unlike other languages:
    # matrix[rows][columns].
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    currentValue = 1
    for c in range(columns):
        if c % 2 == 0:   # values go from the top of column to the bottom
            # matrix[top row->bottom row][current column]
            for r in range(rows):
                matrix[r][columns-1-c] = currentValue
                currentValue += 1
        else:   # values go from the bottom of column to the top
            # matrix[bottom row->top row][current column]
            for r in range(rows):
                matrix[rows-1-r][columns-1-c] = currentValue
                currentValue += 1
    for c in range(rows):
        for r in range(columns):
            print(f"{matrix[c][r]}     ", end="")
        print()
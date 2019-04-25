matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

row_start = 0
row_end = len(matrix)
column_start = 0
column_end = len(matrix[0])
result = []
while row_start < row_end and column_start < column_end:
    for i in range(column_start, column_end):
        result.append(matrix[row_start][i])
    row_start += 1

    for i in range(row_start, row_end):
        result.append(matrix[i][column_end - 1])
    column_end -= 1

    if row_start < row_end:
        for i in range(column_end - 1, column_start - 1, -1):
            result.append(matrix[row_end - 1][i])
        row_end -= 1

    if column_start < column_end:
        for i in range(row_end - 1, row_start - 1, -1):
            result.append(matrix[i][column_start])
        column_start += 1

print(result)



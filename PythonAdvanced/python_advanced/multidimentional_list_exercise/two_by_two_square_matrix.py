rows, cols = [int(x) for x in input().split()]
matrix = [[char for char in input().split()] for _ in range(rows)]
counter = 0

for index_row in range(len(matrix) - 1):
    for index_col in range(len(matrix[index_row]) - 1):
        if matrix[index_row][index_col] == matrix[index_row][index_col + 1] == matrix[index_row + 1][index_col] == \
                matrix[index_row + 1][index_col + 1]:
            counter += 1

print(counter)

#    0 1 2 3
# 0  A B B D
# 1  E B B B
# 2  I J B B

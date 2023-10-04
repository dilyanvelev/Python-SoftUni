rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
maximum_sum = -99999999
maximum_matrix = []

for row in range(len(matrix) - 2):
    for col in range(len(matrix[row]) - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col] + \
                      matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + matrix[row + 2][col] + \
                      matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if current_sum > maximum_sum:
            maximum_sum = current_sum
            maximum_matrix = [
                [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
                [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
                [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
            ]
print(f"Sum = {maximum_sum}")
for row in maximum_matrix:
    print(' '.join(map(str, row)))

# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4

rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
maximum_sum = 0
maximum_matrix = []
for row in range(len(matrix) - 1):
    for col in range(len(matrix[row]) - 1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if current_sum > maximum_sum:
            maximum_sum = current_sum
            maximum_matrix = [
                [matrix[row][col], matrix[row][col + 1]],
                [matrix[row + 1][col], matrix[row + 1][col + 1]]
            ]

for row in maximum_matrix:
    for num in row:
        print(num, end=" ")
    print()
print(maximum_sum)
#     0  1  2  3  4  5
# 0  [7, 1, 3, 3, 2, 1]
# 1  [1, 3, 9, 8, 5, 6]
# 2  [4, 6, 7, 9, 1, 0]

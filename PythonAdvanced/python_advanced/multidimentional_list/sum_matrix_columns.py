rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for col in range(cols):
    total = 0
    for row in range(rows):
        total += matrix[row][col]
    print(total)


#     0  1  2  3  4  5
#  0 [7, 1, 3, 3, 2, 1]
#  1 [1, 3, 9, 8, 5, 6]
#  2 [4, 6, 7, 9, 1, 0]

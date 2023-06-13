rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for col in range(cols):
    total = 0
    for row in range(rows):
        total += matrix[row][col]
    print(total)

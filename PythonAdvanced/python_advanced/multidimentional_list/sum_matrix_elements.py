rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])
total = 0
for row in range(rows):
    for col in range(cols):
        total += matrix[row][col]

print(total)
print(matrix)

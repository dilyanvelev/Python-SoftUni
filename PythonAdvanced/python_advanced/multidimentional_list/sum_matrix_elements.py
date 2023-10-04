rows, cols = [int(x) for x in input().split(", ")]
matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

total = 0

for row in matrix:
    for num in row:
        total += num

print(total)
print(matrix)

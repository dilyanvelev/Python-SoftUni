rows, cols = [int(x) for x in input().split()]
snake = input()
matrix = []
index = 0
for row in range(rows):
    result = ''
    for col in range(cols):
        result += snake[index % len(snake)]
        index += 1
    if row % 2 == 0:
        matrix.append(result)
    else:
        matrix.append(result[::-1])

for submatrix in matrix:
    print(*submatrix, sep='')

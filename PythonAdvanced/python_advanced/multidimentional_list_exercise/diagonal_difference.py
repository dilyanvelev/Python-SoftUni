size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
primary_diagonal = 0
secondary_diagonal = 0

for index in range(len(matrix)):
    primary_diagonal += matrix[index][index]

for index in range(len(matrix)):
    secondary_diagonal += matrix[index][len(matrix) - 1 - index]

print(abs(primary_diagonal - secondary_diagonal))

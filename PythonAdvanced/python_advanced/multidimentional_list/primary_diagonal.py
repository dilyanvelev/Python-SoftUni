n_lines = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n_lines)]
primary_diagonal = 0
for i in range(len(matrix) - 1, 0, -1):
    primary_diagonal += matrix[i][i]

print(primary_diagonal)
#    0     1    2
# 0 [11,   2,   4]
# 1 [4,    5,   6]
# 2 [10,   8, -12]

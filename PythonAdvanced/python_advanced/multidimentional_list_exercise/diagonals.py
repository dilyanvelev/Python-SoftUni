rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
primary_diagonal = 0
secondary_diagonal = 0
prim_diag_list = []
sec_diag_list = []

for index in range(len(matrix)):
    prim_diag_list.append(str(matrix[index][index]))
    primary_diagonal += matrix[index][index]

for index in range(len(matrix)):
    sec_diag_list.append(str(matrix[index][len(matrix) - 1 - index]))
    secondary_diagonal += matrix[index][len(matrix) - 1 - index]

print(f"Primary diagonal: {', '.join(prim_diag_list)}. Sum: {primary_diagonal}")
print(f"Secondary diagonal: {', '.join(sec_diag_list)}. Sum: {secondary_diagonal}")

#    0  1  2
#   __________
# 0 | 1, 2, 3
# 1 | 4, 5, 6
# 2 | 7, 8, 9

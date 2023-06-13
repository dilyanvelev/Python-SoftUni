matrix_size = int(input())
car_number = input()
matrix = []
for line in range(matrix_size):
    line = list(input().split())
    matrix.append(line)
while command != "End":
    command = input()
    for row in matrix:
        for col in row:
            if command == "up":
                row -= 1
            if command == "down":
                row += 1
            if command == "left":
                col -= 1
            if command == "right":
                col += 1

# ['.', '.', '.', '.', '.'],
# ['.', '.', '.', 'T', '.'],
# ['.', '.', '.', '.', '.'],
# ['.', 'T', '.', '.', '.'],
# ['.', '.', 'F', '.', '.']

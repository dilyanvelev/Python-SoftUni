rows = int(input())
matrix = [list(input()) for _ in range(rows)]
searched_symbol = input()
found = False
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == searched_symbol:
            print(f"({row}, {col})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{searched_symbol} does not occur in the matrix")

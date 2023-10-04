rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break
    if len(command.split()) == 5:
        keyword, r1, c1, r2, c2 = command.split()
    else:
        print("Invalid input!")
        continue

    if keyword == 'swap' and 0 <= int(r1) < rows and 0 <= int(c1) < cols and 0 <= int(r2) < rows \
            and 0 <= int(c2) < cols:
        matrix[int(r1)][int(c1)], matrix[int(r2)][int(c2)] = matrix[int(r2)][int(c2)], matrix[int(r1)][int(c1)]
        for row in matrix:
            for col in row:
                print(col, end=' ')
            print()

    else:
        print("Invalid input!")

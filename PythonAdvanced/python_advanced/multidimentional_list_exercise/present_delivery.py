presents = int(input())
size = int(input())
neighborhood = []
santa_pos = []
nice_kids_counter = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    line = input().split()
    if 'V' in line:
        for el in line:
            if el == "V":
                nice_kids_counter.append(el)
    neighborhood.append(line)
    if 'S' in line:
        santa_pos = [row, line.index('S')]
        neighborhood[row][line.index('S')] = '-'

nice_kids = len(nice_kids_counter)
nice_kids_counter = len(nice_kids_counter)

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    row = santa_pos[0] + directions[command][0]
    col = santa_pos[1] + directions[command][1]

    if neighborhood[row][col] == "V":
        nice_kids_counter -= 1
        presents -= 1
    elif neighborhood[row][col] == "C":
        last_santa_pos = [row, col]
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row = row + dr
            new_col = col + dc
            if neighborhood[new_row][new_col] == "X":
                presents -= 1
            if neighborhood[new_row][new_col] == "V":
                nice_kids_counter -= 1
                presents -= 1
            neighborhood[new_row][new_col] = "-"
        neighborhood[row][col] = "-"
        row, col = last_santa_pos[0], last_santa_pos[1]

    neighborhood[row][col] = "-"
    santa_pos = [row, col]

if presents == 0 and nice_kids_counter > 0:
    print("Santa ran out of presents!")

neighborhood[santa_pos[0]][santa_pos[1]] = "S"

for row in neighborhood:
    print(*row)


if nice_kids_counter <= 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_counter} nice kid/s.")


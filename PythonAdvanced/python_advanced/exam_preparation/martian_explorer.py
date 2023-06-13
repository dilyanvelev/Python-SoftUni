SIZE = 6
matrix = []
rover_position = 0

for row in range(SIZE):
    line = matrix.append(line)

    if "E" in line:
        rover_position = [row, line.index("E")]

commands = input().split(", ")
deposits = {
    "Water": 0,
    "Metal": 0,
    "Concrete": 0,
}

deposit_full_name = {
    "W"
}

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while commands:
    command = commands.pop(0)

    rover_position[0] = rover_position[0] + directions[command][0]
    rover_position[1] = rover_position[1] + directions[command][1]

    for i in range(len(rover_position)):

        if rover_position[i] < 0:
            rover_position[i] = SIZE - 1

        elif rover_position[i] == SIZE:
            rover_position[i] = 0

    position = matrix[rover_position[0]][rover_position[1]]

    if position == "W" or position == "M" or position == "C":
        deposits[position] += 1
        print(f"{deposit_full_name[position]} deposit found at ")
    elif position == "R":
        print()

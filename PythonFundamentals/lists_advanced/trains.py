numbers_of_wagons = int(input())
trains = [0] * numbers_of_wagons

while True:
    command = input()
    if command == "End":
        break
    split_command = command.split()

    if split_command[0] == "add":
        trains[-1] += int(split_command[1])
    elif split_command[0] == "insert":
        trains[int(split_command[1])] += int(split_command[2])
    elif split_command[0] == "leave":
        trains[int(split_command[1])] -= int(split_command[2])
print(trains)

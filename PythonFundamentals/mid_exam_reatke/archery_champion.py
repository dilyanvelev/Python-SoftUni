targets_in_fields = list(map(int, input().split('|')))

command = ''
while command != "Game over":
    command = input()
    if command == "Game over":
        continue
    command = command.split('@')
    print(command)
    start_index = int(command[1])
    length = int(command[2])
    print(targets_in_fields[start_index:length + 1])
    for index, num in enumerate(targets_in_fields[start_index:length + 1]):
        if index == length:
            num -= 5
    print(targets_in_fields)

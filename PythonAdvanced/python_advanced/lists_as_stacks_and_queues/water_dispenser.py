from collections import deque

total_liters = int(input())

people = deque()
while True:
    names = input()
    if names == "Start":
        break
    people.append(names)

while True:
    command = input()
    if command == "End":
        break
    line_args = command.split()

    if len(line_args) == 2:
        total_liters += int(line_args[1])
    else:
        liters = int(line_args[0])
        person = people.popleft()
        if liters > total_liters:
            print(f"{person} must wait")
        else:
            print(f"{person} got water")
            total_liters -= liters

print(f"{total_liters} liters left")
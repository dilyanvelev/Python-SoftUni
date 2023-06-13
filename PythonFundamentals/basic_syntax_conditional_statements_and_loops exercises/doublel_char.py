command = ''

while command != "End":

    for char in command:
        print(char * 2, end='')
    print()
    command = input()
    if command == "SoftUni":
        command = input()
        continue


some_string = input()

while True:
    command = input().split()

    if command[0] == "Easter":
        break

    if command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        some_string = some_string.replace(current_char, new_char)
        print(some_string)

    elif command[0] == "Remove":
        substring = command[1]
        some_string = some_string.replace(substring, '')
        print(some_string)

    elif command[0] == 'Includes':
        if command[1] in some_string:
            print(True)
        else:
            print(False)

    elif command[0] == 'Change':
        if command[1] == 'Upper':
            some_string = some_string.upper()

        elif command[1] == 'Lower':
            some_string = some_string.lower()

        print(some_string)

    elif command[0] == 'Reverse':
        start_index = int(command[1])
        end_index = int(command[2])
        pre_rev_string = some_string[start_index:end_index+1]
        reverse_string = ''.join(reversed(pre_rev_string))
        print(reverse_string)
#100/100

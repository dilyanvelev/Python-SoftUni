some_string = input()

while True:
    command = input().split()

    if command[0] == "Finish":
        break

    if command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        some_string = some_string.replace(current_char, new_char)
        print(some_string)

    elif command[0] == "Cut":

        if -50 < int(command[1]) <= 0 or int(command[2]) >= len(some_string) < 150:
            print("Invalid indices!")
            continue

        cut_ratio = some_string[int(command[1]):int(command[2]) + 1]
        some_string = some_string.replace(cut_ratio, '')
        print(some_string)

    elif command[0] == "Make":

        if command[1] == 'Upper':
            some_string = some_string.upper()

        elif command[1] == 'Lower':
            some_string = some_string.lower()

        print(some_string)

    elif command[0] == "Check":

        if command[1] not in some_string:
            print(f"Message doesn't contain {str(command[1])}")
        else:
            print(f"Message contains {str(command[1])}")

    elif command[0] == "Sum":

        if -50 < int(command[1]) <= 0 or int(command[2]) >= len(some_string) < 150:
            print("Invalid indices!")
            continue

        substring = some_string[int(command[1]):int(command[2]) + 1]
        print(sum(ord(ch) for ch in substring))
#oyeeeeee beibi 100/100




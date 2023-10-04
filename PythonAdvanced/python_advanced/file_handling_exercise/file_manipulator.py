from os import remove

while True:
    command = input()
    if command == "End":
        break

    command = command.split('-')

    if command[0] == "Create":
        with open(f'files/{command[1]}', 'w') as file:
            file.write('')

    elif command[0] == "Add":
        with open(f'files/{command[1]}', 'a') as file:
            file.write(f"{command[2]}\n")

    elif command[0] == "Replace":
        try:
            with open(f'files/{command[1]}', 'r+') as file:
                text = file.readlines()

                for i in range(len(text)):
                    text[i] = text[i].replace(command[2], command[3])

                file.write(''.join(text))
        except FileNotFoundError:
            print("An error occurred")

    elif command[0] == "Delete":
        try:
            remove(f"files/{command[1]}")
        except FileNotFoundError:
            print("An error occurred")

number_of_inputs = int(input())
registration_dict = {}
for _ in range(number_of_inputs):
    command = input().split()

    action = command[0]

    if action == "register":
        username = command[1]
        license_plate = command[2]

        if username not in registration_dict:
            registration_dict[username] = license_plate
            print(f"{username} registered {registration_dict[username]} successfully")
        else:
            print(f"ERROR: already registered with plate number {registration_dict[username]}")
    if action == "unregister":
        username = command[1]
        if username not in registration_dict:
            print(f"ERROR: user {username} not found")
        else:
            registration_dict.pop(username)
            print(f"{username} unregistered successfully")

for key, value in registration_dict.items():
    print(f"{key} => {value}")

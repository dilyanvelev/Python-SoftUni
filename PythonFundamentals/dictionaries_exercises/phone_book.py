info = input().split("-")
dictionary = {}
while not info[0].isdigit():
    name = info[0]
    phone_number = info[1]

    if name not in dictionary:
        dictionary[name] = phone_number
    dictionary[name] = phone_number

    info = input().split("-")

info = int(info[0])

for i in range(info):
    searched_name = input()
    if searched_name in dictionary:
        print(f"{searched_name} -> {dictionary[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")

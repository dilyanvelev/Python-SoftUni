courses_dictionary = {}

while True:
    command = input()
    if command == "end":
        break
    info = command.split(" : ")
    course = info[0]
    name = info[1]

    if course not in courses_dictionary:
        courses_dictionary[course] = [name]
    else:
        courses_dictionary[course].append(name)
# {'Programming Fundamentals': ['John Smith', 'Linda Johnson'],
#  'JS Core': ['Will Wilson'],
#  'Java Advanced': ['Harrison White']}

for key, value in courses_dictionary.items():
    print(f"{key}: {len(value)}")
    for names in value:
        print(f"-- {names}")
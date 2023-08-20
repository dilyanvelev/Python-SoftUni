companies_dictionary = {}
prev_id = ""
while True:

    command = input()

    if command == "End":
        break

    info = command.split(" -> ")
    company_name = info[0]

    employee_id = info[1]

    if company_name not in companies_dictionary:
        companies_dictionary[company_name] = [employee_id]
    else:
        if employee_id not in companies_dictionary[company_name]:
            companies_dictionary[company_name].append(employee_id)

for key, value in companies_dictionary.items():
    print(key)
    for id in value:
        print(f"-- {id}")

employees_happiness = input().split()
factor = int(input())

multiplied_list = [int(num) * factor for num in employees_happiness]

average_sum = sum(multiplied_list) / len(employees_happiness)
filtered_list = [num for num in multiplied_list if num >= average_sum]

if len(filtered_list) >= len(employees_happiness) / 2:
    print(f"Score: {len(filtered_list)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_list)}/{len(employees_happiness)}. Employees are not happy!")

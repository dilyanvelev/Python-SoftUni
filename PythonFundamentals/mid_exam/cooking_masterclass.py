from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())
free_packages = 0

for num in range(0, students, 5):
    if students < 5:
        continue
    else:
        free_packages += 1

set_for_one_student = apron_price * (students + ceil(students * 0.2)) + (egg_price * 10 * students) + flour_price * (
        students - free_packages)
if budget >= set_for_one_student:

    print(f"Items purchased for {set_for_one_student:.2f}$.")
else:
    absolute_price = abs(budget - set_for_one_student)

    print(f"{absolute_price:.2f}$ more needed.")

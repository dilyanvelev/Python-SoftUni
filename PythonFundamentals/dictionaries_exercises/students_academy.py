number_of_students = int(input())
grades_dict = {}
for _ in range(number_of_students):
    name = input()
    grade = float(input())

    if name not in grades_dict:
        grades_dict[name] = [grade]
    else:
        grades_dict[name].append(grade)

for key, value in grades_dict.items():
    average_grade = sum(value)/len(value)
    if average_grade >= 4.5:
        print(f"{key} -> {average_grade:.2f}")

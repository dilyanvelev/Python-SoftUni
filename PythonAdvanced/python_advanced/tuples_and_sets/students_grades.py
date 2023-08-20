n_lines = int(input())
students_dict = {}
for _ in range(n_lines):
    name, grade = input().split()
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(float(grade))

for name, grades in students_dict.items():
    average_grade = sum(grades) / len(grades)
    grades_list = [str(f"{grade:.2f}") for grade in grades]
    print(f"{name} -> {' '.join(grades_list)} (avg: {average_grade:.2f})")

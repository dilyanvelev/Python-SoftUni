student_info = input().split(":")
students_by_course = {}

while len(student_info) > 1:
    name, student_id, course = student_info

    if course not in students_by_course:
        students_by_course[course] = {name: student_id}
    students_by_course[course].update({name: student_id})
    student_info = input().split(":")

# {'programming basics': {'Peter': '123'},
# 'fundamentals': {'John': '5622', 'Maya': '89', 'Lilly': '633'}}

if "_" in student_info[0]:
    student_info = student_info[0].replace("_", " ")
else:
    student_info = student_info[0]

for key in students_by_course:
    if key == student_info:
        for unpacked_name, unpacked_id in students_by_course[student_info].items():
            print(f"{unpacked_name} - {unpacked_id}")

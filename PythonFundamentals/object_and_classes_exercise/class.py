class Class:
    __students_count = 22

    def __init__(self, name: str):
        self.name = name
        self.average_grade = 0
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        while Class.__students_count > 0:
            self.students.append(name)
            self.grades.append(grade)
            Class.__students_count -= 1
            break

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)

print(a_class)

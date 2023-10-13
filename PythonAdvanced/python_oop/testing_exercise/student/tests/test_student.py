from unittest import TestCase, main

from project.student import Student


class StudentTests(TestCase):
    def setUp(self):
        self.student = Student("Student")

    def test_initialization(self):
        self.assertEqual('Student', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_courses_initialization_if_it_is_not_None(self):  # useless test case but OK
        self.student.courses = {'course': [6, 6, 6]}
        result = self.student.courses
        self.assertEqual(result, self.student.courses)

    def test_adding_course_if_not_in_courses(self):
        result = self.student.enroll('course', 'X', "D")
        self.assertEqual("Course has been added.", result)

    def test_adding_course_and_notes_if_course_in_courses(self):
        self.student.courses = {'course': []}
        result = self.student.enroll('course', ['X', 'C'])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({'course': ['X', 'C']}, self.student.courses)

    def test_adding_course_and_course_notes_if_course_not_in_courses(self):
        result = self.student.enroll('course1', ['X'])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'course1': ['X']}, self.student.courses)

    def test_add_notes_if_course_not_int_courses_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('course', ['X'])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_if_course_in_courses(self):
        self.student.courses = {'course': []}
        result = self.student.add_notes('course', 'X')
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({'course': ['X']}, self.student.courses)

    def test_leave_course_if_course_not_exist_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('course')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_if_course_exist(self):
        self.student.courses = {'course': []}
        result = self.student.leave_course('course')
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)


if __name__ == '__main__':
    main()

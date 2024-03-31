from unittest import TestCase, main
from project.student import Student
class TestStudent(TestCase):

    def setUp(self):
        self.student = Student('NoCoursesStudent')
        self.student2 = Student('CoursesStudent', {'Math': [1, 2, 3]})

    def test_check_for_correct_init(self):
        self.assertEqual(self.student.courses, {})
        self.assertEqual(self.student2.courses, {'Math': [1, 2, 3]})


    def test_enroll_in_the_same_course_updates_new_notes(self):
        result = self.student2.enroll("Math", [4, 5])

        self.assertEqual('Course already added. Notes have been updated.', result)
        self.assertEqual(self.student2.courses["Math"],
                         [1, 2, 3, 4, 5])

    def test_enroll_in_new_course_without_third_param_adds_note_to_the_course(self):
        result = self.student.enroll("Math",
                                     ['c', 2, 3])
        self.assertEqual(result, 'Course and course notes have been added.')
        self.assertEqual(self.student.courses['Math'], ['c', 2, 3])


    def test_enroll_in_new_course_with_third_param_Y_adds_note_to_the_course(self):
        result = self.student.enroll("Math",
                                     ['c', 2, 3], 'Y')
        self.assertEqual(result, 'Course and course notes have been added.')
        self.assertEqual(self.student.courses['Math'], ['c', 2, 3])

    def test_enroll_in_new_course_with_NO_param_does_not_adds_note_to_the_course(self):
        result = self.student.enroll("Math",
                                     ['c', 2, 3], 'N')
        self.assertEqual(result, 'Course has been added.')
        self.assertEqual(self.student.courses['Math'], [])

    def test_if_course_and_notes_added_correctly(self):
        result = self.student2.add_notes("Math",
                                         4)
        self.assertEqual(result, 'Notes have been updated')
        self.assertEqual(self.student2.courses['Math'], [1, 2, 3, 4])

    def test_no_such_course_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Math", [1, 2])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_removes_correctly_the_name(self):
        result = self.student2.leave_course('Math')
        self.assertEqual("Course has been removed", result)

    def test_leave_course_raises_exception_when_no_such_course(self):

        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Math')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == '__main__':
    main()
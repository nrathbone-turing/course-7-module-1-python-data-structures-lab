# This module contains functions for filtering student data.

from lib.student_data import students

def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    - Match major case-insensitively
    - student_list is a list of tuples: (id, name, major)
    """
    return [student for student in student_list if student[2].lower() == major.lower()]
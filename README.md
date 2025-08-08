# Student Data Management System Lab
A modular Python application for managing and processing student records using built-in data structures like lists, tuples, sets, and generator expressions.

## Features
- Store student records using tuples inside lists.
- Filter students by major using list comprehensions.
- Display student information in a clean, formatted way.
- Extract unique student majors using set comprehensions.
- Lazily generate students by major using a generator expression.

## File Structure
```
lib/
├── __init__.py            # Module marker
├── data_generator.py      # Generator expression for streaming student data
├── data_processing.py     # Formatting and display functions
├── filters.py             # List comprehension logic for filtering students
├── set_operations.py      # Unique major extraction using set comprehension
└── student_data.py        # Contains raw student records as tuples

```

## Running Tests
Install dependencies and activate your virtual environment:
```
pipenv install
pipenv shell
pytest -x
```

## Example Usage

```
from lib.student_data import students
from lib.filters import filter_students_by_major
from lib.data_processing import display_students
from lib.set_operations import unique_majors
from lib.data_generator import student_generator

# Filter CS majors
cs_students = filter_students_by_major(students, "Computer Science")

# Display formatted data
display_students(cs_students)

# Show unique majors
print(unique_majors(students))

# Use generator to process one at a time
cs_gen = student_generator(students, "Computer Science")
print(next(cs_gen))
```

## Learning Objectives Demonstrated
- Use of Python sequences (lists & tuples)
- List comprehensions for filtering
- Set comprehensions for uniqueness
- Generator expressions for lazy evaluation
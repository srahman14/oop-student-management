"""
validation.py
--------------
Provides validation logic for student IDs used throughout the Student Management System.

This module defines a single utility function, `validate_student_id`, which validates
the format and existence of student IDs for different operations (add, update, delete).
It raises appropriate custom exceptions (`InvalidIDException`, `DuplicateIDException`) 
based on the context of the operation.

Flexible boolean flags (`for_deletion`, `for_student`, `for_minors`) are used to determine
whether the ID must already exist or must be unique depending on the operation.

Part of Task 4: Implement Exception Handling.
Also supports validation workflows for Task 3 (CRUD) and Task 5 (File Storage).
"""

from exceptions import DuplicateIDException, InvalidIDException 
from storage import load_students
from models.student import Student

# Function for validating a student
# Parameters:
# - student_id
# - for_deletion, used when a student is being deleted
# - for_student, used when updating a student
# - for_minors, used when updating an undergrad
# - for_updating, used when updating in the main-menu
def validate_student_id(student_id, for_deletion=False, for_student=False, for_minors=False, for_updating=False):
    if str(student_id)[0] == "0":
        raise InvalidIDException(f"{student_id} is not a valid entry. ID cannot begin with 0")
    # Check if the student_id is only numbers
    if type(student_id) != int:
        raise InvalidIDException(f"{student_id} is not a valid entry. ID can only consist of numbers")
    # Check if the student_id is 0 or None (i.e. unset/undefined)
    if student_id == 0 or student_id is None:
        raise InvalidIDException(f"{student_id} is not a valid entry. ID cannot be undefined")
    # Check if the student_id is less than 6 characters
    if len(str(student_id).strip()) < 6:
        raise InvalidIDException(f"{student_id} is not a valid entry. ID must be 6 digits minimum")
    
    # This is used to update minors in the student_operations.py file, we only need to validate the ID, but
    # we don't need to check if it already exists, as this is implied. So we return true before that check.
    # Even though both, for_minors and for_student are used for the same update function, I set them as separate
    # paramaters for more clarity of what is being validated.
    if for_minors or for_student:
        return True

    # Check for an ID which already exists in the database (i.e. duplicate ID entry)
    students_data = load_students()
    # All existing student IDs
    existing_ids = {s.get_student_id() for s in students_data}

    if for_deletion or for_updating:
        # When deleting, ensure the student ID exists
        if student_id not in existing_ids:
            raise InvalidIDException(f"Student ID {student_id} does not exist")
    else:
        # When adding, ensure the student ID is unique
        if student_id in existing_ids:
            raise DuplicateIDException(f"Student ID {student_id} already exists. ID must be unique")
    
    # if no conditions met, then the ID is valid
    return True
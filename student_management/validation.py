from exceptions import DuplicateIDExcption, InvalidIDException 
from storage import load_students
from models.student import Student

def validate_student_id(student_id):
    # Check if the student_id is only numbers
    if type(student_id) != int:
        raise InvalidIDException(f"{student_id} is not a valid entry. ID can only consist of numbers")
    # Check if the student_id is 0 or None (i.e. unset/undefined)
    if student_id == 0 or student_id is None:
        raise InvalidIDException(f"{student_id} is not a valid entry. ID cannot be undefined")
    # Check if the student_id is less than 6 characters
    if len(str(student_id).strip()) < 6:
        raise InvalidIDException(f"{student_id} is not a valid entry. ID must be 6 digits minimum")
    

    # Check for an ID which already exists in the database (i.e. duplicate ID entry)
    students_data = load_students()

    duplicate_count = sum(1 for s in students_data if s.get_student_id() == student_id)
    if duplicate_count > 0:
        raise DuplicateIDExcption(f"One student with ID: {student_id}. ID must be unique")
    
    # if no conditions met, then the ID is valid
    return True
from exceptions import DuplicateIDException, InvalidIDException 
from storage import load_students
from models.student import Student

def validate_student_id(student_id, for_deletion=False, for_minors=False):
    # Check if the student_id is only numbers
    if type(student_id) != int:
        raise InvalidIDException(f"{student_id} is not a valid entry. ID can only consist of numbers")
    # Check if the student_id is 0 or None (i.e. unset/undefined)
    if student_id == 0 or student_id is None:
        raise InvalidIDException(f"{student_id} is not a valid entry. ID cannot be undefined")
    # Check if the student_id is less than 6 characters
    if len(str(student_id).strip()) < 6:
        raise InvalidIDException(f"{student_id} is not a valid entry. ID must be 6 digits minimum")
    
    if for_minors:
        return True

    # Check for an ID which already exists in the database (i.e. duplicate ID entry)
    students_data = load_students()
    existing_ids = {s.get_student_id() for s in students_data}

    if for_deletion:
        # When deleting, ensure the student ID exists
        if student_id not in existing_ids:
            raise InvalidIDException(f"Student ID {student_id} does not exist and cannot be deleted")
    else:
        # When adding, ensure the student ID is unique
        if student_id in existing_ids:
            raise DuplicateIDException(f"Student ID {student_id} already exists. ID must be unique")
            
    # duplicate_count = sum(1 for s in students_data if s.get_student_id() == student_id)
    # if duplicate_count > 0 and for_deletion is True: 
    #     raise DuplicateIDException(f"One student with ID: {student_id}. ID must be unique")
    
    # if no conditions met, then the ID is valid
    return True
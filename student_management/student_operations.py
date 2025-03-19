import json
import re
from models.student import Student
from models.student import StudentEncoder
from models.student import StudentDecoder
from exceptions import DuplicateIDExcption
from exceptions import InvalidIDException

def validate_student_id(student_id):
    # Check if the student_id is only numbers
    if type(student_id) != int:
        raise InvalidIDException(f"{student_id} is not a valid entry. ID can only consist of numbers")
    # Check if the student_id is 0 or None (i.e. unset/undefined)
    if student_id == 0 or student_id is None:
        raise InvalidIDException(f"{student_id} is not a valid entry. ID cannot be undefined")
    # Check if the student_id is less than 6 characters
    if not bool(re.fullmatch(r"\d{6}", str(student_id))):
        raise InvalidIDException(f"{student_id} is not a valid entry. ID must be 6 digits minimum")

    # Check for an ID which already exists in the database (i.e. duplicate ID entry)
    try:
        with open("student_management/students.json", "r") as f:
            students_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        students_data = [] # IF the file does not exist or is empty, start with an empty list

    duplicate_count = sum(1 for s in students_data if s['student_id'] == student_id)
    if duplicate_count > 1:
        raise DuplicateIDExcption(f"More than one student with ID: {student_id}. {duplicate_count} number of students with ID: {student_id}")
    
    # if no conditions met, then the ID is valid
    return True

def add_student(student_id, name, age, courses):
    try:
        validate_student_id(student_id)
        try:
            with open("student_management/students.json", "r") as f:
                students_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            students_data = [] # IF the file does not exist or is empty, start with an empty list

        if not validate_student_id(student_id):
            return
        else:
            new_student = Student(student_id, name, age, courses)
            students_data.append(new_student)

        with open("student_management/students.json", "w") as f:
            json.dump(students_data, f, cls=StudentEncoder, indent=4)

        print(f"Student {student_id} has been added successfully!")
    except InvalidIDException as e:
        print(f"Error: {e}")
    except DuplicateIDExcption as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        
def list_all_students():
    try:
        with open("student_management/students.json", "r") as f:
            students_data = json.load(f, cls=StudentDecoder)
    except (FileNotFoundError, json.JSONDecodeError):
        students_data = [] # IF the file does not exist or is empty, start with an empty list

    for i in students_data:
        print(i)

def update_student(student_id, new_name=None, new_age=None, old_course=None, new_course=None):
    if new_name is None and new_age is None and new_course is None: return "Nothing has been updated"

    try:
        validate_student_id(student_id)
    except InvalidIDException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")        

    try:
        with open("student_management/students.json", "r") as f:
            students_data = json.load(f, cls=StudentDecoder)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No students found.")
        return

    # Flag to track if student to be updated found
    student_found = False
    for student in students_data:
        if student.get_student_id() == student_id:
            student_found = True

            if new_name == student.get_name():
                print(f"Student name {new_name} with ID: {student_id} is already {new_name}. Cannot update.")
            elif new_name is not None:
                student.update_name(new_name)
                print(f"Student Name for {student_id} updated successfully!")
            if new_age == student.get_age():
                print(f"Student {student.get_name()} with ID: {student_id} age is already {new_age}. Cannot update.")
            elif new_age is not None:
                student.update_age(new_age)
                print(f"Student Age for {student_id} updated successfully!")
            if old_course and new_course:
                student.update_courses(old_course, new_course)

            print(f"Student with ID: {student_id} updated successfully for valid entries")
            break

    if not student_found:
        print(f"Error: Student with ID {student_id} not found.")
        return

    try:
        with open("student_management/students.json", "w") as f:
            json.dump(students_data, f, indent=4, cls=StudentEncoder)
    except Exception as e:
        print(f"Error writing to file: {e}")           

def add_new_courses(student_id, new_courses):
    try:
        validate_student_id(student_id)
    except InvalidIDException as e:
        print(f"Error: {e}")
    except DuplicateIDExcption as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}") 

    try:
        with open("student_management/students.json", "r") as f:
            students_data = json.load(f, cls=StudentDecoder)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No students found.")
        return

    # Flag to track if student to be updated found
    student_found = False
    for student in students_data:
        if student.get_student_id() == student_id:
            student_found = True

            if new_courses and len(new_courses) > 0:
                student.add_courses(new_courses)
            else:
                print("Error: No courses to add")
            break

    if not student_found:
        print(f"Error: Student with ID {student_id} not found.")
        return

    try:
        with open("student_management/students.json", "w") as f:
            json.dump(students_data, f, indent=4, cls=StudentEncoder)
    except Exception as e:
        print(f"Error writing to file: {e}")      


def remove_course(student_id, remove_this_course):
    try:
        validate_student_id(student_id)
    except InvalidIDException as e:
        print(f"Error: {e}")
    except DuplicateIDExcption as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}") 

    try:
        with open("student_management/students.json", "r") as f:
            students_data = json.load(f, cls=StudentDecoder)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No students found.")
        return

    # Flag to track if student to be updated found
    student_found = False
    for student in students_data:
        if student.get_student_id() == student_id:
            student_found = True

            if remove_this_course and len(remove_this_course) > 0:
                student.remove_course(remove_this_course)
                break

    if not student_found:
        print(f"Error: Student with ID {student_id} not found.")
        return

    try:
        with open("student_management/students.json", "w") as f:
            json.dump(students_data, f, indent=4, cls=StudentEncoder)
    except Exception as e:
        print(f"Error writing to file: {e}")      

def del_student(student_id):
    try:
        validate_student_id(student_id)
    except InvalidIDException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Open JSON
    try:
        with open("student_management/students.json", "r") as f:
            students_data = json.load(f, cls=StudentDecoder)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No students found.")
        return

    student_found = False
    final_check = ""
    for i, student in enumerate(students_data):
        if student.get_student_id() == student_id:
            student_found = True

            final_check = input(f"\nFINAL WARNING:\nAre you sure you want to delete student with ID: {student_id}? (y/n) ")
            if final_check.strip().lower() == "y":
                del students_data[i]
                break
            else:
                print(f"Student with ID {student_id} not deleted")
                break
    
    if not student_found:
        raise InvalidIDException(f"Error: Student with ID {student_id} not found")

    # Close JSON
    if final_check == "y":
        try:
            with open("student_management/students.json", "w") as f:
                json.dump(students_data, f, indent=4, cls=StudentEncoder)
            print(f"Student with ID {student_id} has been deleted")
        except Exception as e:
            print(f"Error writing to file {e}")
        


import json
import re
from models.student import Student
from models.undergraduate import Undergraduate
from storage import load_students, save_students
from exceptions import DuplicateIDException, InvalidIDException 
from validation import validate_student_id


def find_student_by_id(student_id):
    students_data = load_students()
    for student in students_data:
        # If student ID matches return student
        if student.get_student_id() == student_id:
            return student
    # Default
    return None

def add_student(student_id: int, name: str, age: int, courses: list, undergrad: bool, minor: list):
    try:
        # Validate ID 
        validate_student_id(student_id)
        
        students_data = load_students()
        # If student is an undergrad, use the undergrad class
        if undergrad:
            new_student = Undergraduate(student_id, name, age, courses, minor)
        else:
            new_student = Student(student_id, name, age, courses)
        students_data.append(new_student)

        save_students(students_data)
        print(f"Student {student_id} has been added successfully!")

    except InvalidIDException as e:
        print(f"Error: {e}")
    except DuplicateIDException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Print out all the students
def list_all_students():
    students_data = load_students()
    for i in students_data:
        print(i)

# Print out a student
def list_a_student(student_id):
    students_data = load_students()
    for student in students_data:
        if student.get_student_id() == student_id:
            print(student)

def update_student(student_id, new_name=None, new_age=None, old_course=None, new_course=None, minors=None):
    # If all entries left as none
    if all(value is None for value in [new_name, new_age, new_course, minors]):
        return "Nothing to update"
    try:
        if minors:
            # for_minors parameter is set to true here, as we are updating a undergrad
            validate_student_id(student_id, for_minors=True)
        else:
            # for_student parameter is set to true here, as we are updating a student without a minor
            validate_student_id(student_id, for_student=True)
    except InvalidIDException as e:
        print(f"Error: {e}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")        
        return

    students_data = load_students()
    if students_data is None:
        return

    # Flag to track if student to be updated found
    student_found = False
    for student in students_data:
        # Find the student to update
        if student.get_student_id() == student_id:
            student_found = True
        
            # Verify each paramater
            # Check if name to update is already the student's name
            if new_name == student.get_name():
                print(f"Student name {new_name} with ID: {student_id} is already {new_name}. Cannot update.")
            elif new_name is not None:
                student.update_name(new_name)
                print(f"Student Name for {student_id} updated successfully!")
            # Check if age to update is already the student's age
            if new_age == student.get_age():
                print(f"Student {student.get_name()} with ID: {student_id} age is already {new_age}. Cannot update.")
            elif new_age is not None:
                student.update_age(new_age)
                print(f"Student Age for {student_id} updated successfully!")
            # Check if old_course and new_course is not None
            if old_course and new_course:
                student.update_courses(old_course, new_course)
                print(f"Student Course for {student_id} updated {old_course} -> {new_course}")
            # Check if minors is not none and the student is a undergrad
            if minors is not None and isinstance(student, Undergraduate):
                    student.update_minors(minors)
            elif minors is not None:
                print(f"Error: Student with ID {student_id} is not an undergraduate. Cannot update minors, as they don't exist")
            
            print(f"Student with ID: {student_id} updated successfully for valid entries")
            break
    
    if not student_found:
        print(f"Error: Student with ID {student_id} not found.")
        return

    save_students(students_data)    

def add_new_courses(student_id, new_courses):
    try:
        validate_student_id(student_id, for_student=True)
    except InvalidIDException as e:
        print(f"Error: {e}")
    except DuplicateIDException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}") 

    students_data = load_students()

    # Flag to track if student to be updated found
    student_found = False
    for student in students_data:
        # Find the student to add new courses to
        if student.get_student_id() == student_id:
            student_found = True    

            # Verify new_courses is not empty and not none
            if new_courses and len(new_courses) > 0:
                student.add_courses(new_courses)
            else:
                print("Error: No courses to add")
            break

    if not student_found:
        print(f"Error: Student with ID {student_id} not found.")
        return

    save_students(students_data)    

def add_new_minors(student_id, new_minors):
    try:
        validate_student_id(student_id, for_minors=True)
    except (InvalidIDException, DuplicateIDException) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}") 

    students_data = load_students()

    # Flag to track if student to be updated found
    student_found = False
    for student in students_data:
        # Find the student to add new courses to
        if student.get_student_id() == student_id:
            student_found = True

            # Verify the user is an undergrad
            if isinstance(student, Undergraduate):
                # Verify new_minors is not empty/none
                if new_minors:
                    student.add_minors(new_minors)
                    print(f"Added minors for Student {student_id}: {', '.join(new_minors)}")
                else:
                    print("Error: No minors to provided.")
            else:
                print(f"Error: Student with ID {student_id} is not an undergradute. Cannot add minors.")
            break

    if not student_found:
        print(f"Error: Student with ID {student_id} not found.")
        return

    save_students(students_data) 

def remove_course(student_id, remove_this_course):
    try:
        validate_student_id(student_id)
    except InvalidIDException as e:
        print(f"Error: {e}")
    except DuplicateIDException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}") 

    students_data = load_students()

    # Flag to track if student to be updated found
    student_found = False
    for student in students_data:
        # Find the student to remove a course from
        if student.get_student_id() == student_id:
            student_found = True
            # Verify the course to remove is not empty
            if remove_this_course and len(remove_this_course) > 0:
                student.remove_course(remove_this_course)
                break

    if not student_found:
        print(f"Error: Student with ID {student_id} not found.")
        return

    save_students(students_data)

def remove_minor(student_id, remove_this_minor):
    try:
        validate_student_id(student_id, for_minors=True)
    except (InvalidIDException, DuplicateIDException) as e:
        print(f"Error: {e}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}") 
        return

    students_data = load_students()

    # Flag to track if student to be updated found
    student_found = False
    for student in students_data:
        # Find the student to remove minors from 
        if student.get_student_id() == student_id:
            student_found = True   

            # Verify the student is an undergrad
            if isinstance(student, Undergraduate):
                # Verify the minor is not empty/none
                if remove_this_minor:
                    student.remove_minor(remove_this_minor.capitalize())
            else:
                print(f"Error: Student with ID {student_id} is not an undergradute. Cannot add minors.")
                return
            break   

    if not student_found:
        print(f"Error: Student with ID {student_id} not found.")
        return

    save_students(students_data)

def del_student(student_id):
    students = load_students()  # Load current students

    # for_deletion parameter is passed as true
    validate_student_id(student_id, for_deletion=True)
    # updated_students here is a list of all students without the student_id to delete
    updated_students = [s for s in students if s.get_student_id() != student_id]
    
    # Check if student was actually removed
    if len(updated_students) == len(students):
        print(f"Error: Student ID {student_id} not found.")
        return

    # Save the updated student list (ensuring only one student is removed)
    save_students(updated_students)
    print(f"Student ID {student_id} deleted successfully.")


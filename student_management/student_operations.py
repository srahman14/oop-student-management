import json
import re
from models.student import Student
from models.undergraduate import Undergraduate
from storage import load_students, save_students
from exceptions import DuplicateIDExcption, InvalidIDException 
from validation import validate_student_id


def find_student_by_id(student_id):
    students_data = load_students()
    for student in students_data:
        if student.get_student_id() == student_id:
            return student
    return None
def add_student(student_id: int, name: str, age: int, courses: list, undergrad: bool, minor: list):
    try:
        validate_student_id(student_id)
        
        students_data = load_students()
        if undergrad:
            new_student = Undergraduate(student_id, name, age, courses, minor)
        else:
            new_student = Student()
        students_data.append(new_student)

        save_students(students_data)
        print(f"Student {student_id} has been added successfully!")

    except InvalidIDException as e:
        print(f"Error: {e}")
    except DuplicateIDExcption as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        
def list_all_students():
    students_data = load_students()
    for i in students_data:
        print(i)
        
def list_a_student(student_id):
    students_data = load_students()
    for student in students_data:
        if student.get_student_id() == student_id:
            print(student)
        
def update_student(student_id, new_name=None, new_age=None, old_course=None, new_course=None):
    if new_name is None and new_age is None and new_course is None: return "Nothing to update"

    try:
        validate_student_id(student_id)
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

    save_students(students_data)    

def add_new_courses(student_id, new_courses):
    try:
        validate_student_id(student_id)
    except InvalidIDException as e:
        print(f"Error: {e}")
    except DuplicateIDExcption as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}") 

    students_data = load_students()

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

    save_students(students_data)    


def remove_course(student_id, remove_this_course):
    try:
        validate_student_id(student_id)
    except InvalidIDException as e:
        print(f"Error: {e}")
    except DuplicateIDExcption as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}") 

    students_data = load_students()

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

    save_students(students_data)

def del_student(student_id):
    try:
        validate_student_id(student_id)
    except InvalidIDException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Open JSON
    students_data = load_students()


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
        print(f"Error: Student with ID {student_id} not found")

    # Close JSON
    if final_check == "y":
        try:
            save_students(load_students)
            print(f"Student with ID {student_id} has been deleted")
        except Exception as e:
            print(f"Error writing to file {e}")
        


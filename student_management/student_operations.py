"""
student_operations.py
---------------------
Handles CRUD operations for student records.

Includes logic to add, update, delete, and list students. Validates
student IDs before operations and uses exception handling for errors.

Part of Task 3: Develop Student Management Operations.
Also supports Tasks 4 (Exception Handling) and Task 5 (File Storage Integration).
"""

from models.student import Student
from models.undergraduate import Undergraduate
from storage import load_students, save_students
from exceptions import DuplicateIDException, InvalidIDException 
from validation import validate_student_id


# Function to find student by ID
def find_student_by_id(student_id):
    students_data = load_students()

    for student in students_data:
        if student.get_student_id() == student_id:
            return student
    return None

# Function to create a new student (Crud - Create)
# Parameters:
# - student_id, name, age, courses, minor (if a student is an undergraduate)
# - undergrad -> bool (verifies if a student is an undergrad or not to decide which class to use Student/Undergraduate)
def add_student(student_id: int, name: str, age: int, courses: list, undergrad: bool, minor: list):
    try:
        # Validate the student ID, verify it meets reqs. (unique, minimum chars etc.)
        validate_student_id(student_id)
        
        # Load students from students.json
        students_data = load_students()
        # If student is an undergrad, then use undergraduate class, else Student class
        if undergrad:
            new_student = Undergraduate(student_id, name, age, courses, minor)
        else:
            new_student = Student(student_id, name, age, courses)
        # Add the new student to the existing student database
        students_data.append(new_student)

        # Save the new students by passing the new list of students as a parameter
        save_students(students_data)
        print(f"Student {student_id} has been added successfully!")

    except InvalidIDException as e:
        print(f"Error: {e}")
    except DuplicateIDException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Function for listing all students in the student database (cRud - Read)
def list_all_students():
    # Load the students
    students_data = load_students()
    for i in students_data:
        # This uses the __str__ format for displaying student objects, defined in the Student class
        print(i)

# Function for listing a specific student by student_id (cRud - Read)        
def list_a_student(student_id):
    # Load students
    students_data = load_students()
    # Go thruogh every student, and find matching student id
    for student in students_data:
        if student.get_student_id() == student_id:
            print(student)

# Function for updating a student - (crUd - Update)
# Paramters:
# - student_id, new_name, new_age, old_course, new_course, minors (for students who are undergrads)
def update_student(student_id, new_name=None, new_age=None, old_course=None, new_course=None):
    # Base case, if all the parameters are left as none, return
    if new_name is None and new_age is None and new_course is None: return "Nothing to update"

    try:
        # Validate the student_id with 'for_update' param to avoid raising error for duplicate ID
        validate_student_id(student_id, for_student=True)
    except InvalidIDException as e:
        print(f"Error: {e}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")        
        return

    students_data = load_students()
    # If student data cannot be found, return to the main menu
    if students_data is None:
        return

    # Flag to track if student to be updated found
    student_found = False
    # Loop through each student till desired student found
    for student in students_data:
        if student.get_student_id() == student_id:
            student_found = True

            # Use if statements for each param to verify that it is not none, i.e. a valid entry
            # Compare for name and age if they are already the student's name or age
            if new_name == student.get_name():
                print(f"Student name {new_name} with ID: {student_id} is already {new_name}. Cannot update.")
            elif new_name is not None:
                student.update_name(new_name)
            if new_age == student.get_age():
                print(f"Student {student.get_name()} with ID: {student_id} age is already {new_age}. Cannot update.")
            elif new_age is not None:
                student.update_age(new_age)
                print(f"Student Age for {student_id} updated successfully!")
            if old_course and new_course:
                student.update_courses(old_course, new_course)
            print(f"Student with ID: {student_id} updated for valid entries")
            break
        
    if not student_found:
        print(f"Error: Student with ID {student_id} not found.")
        return

    save_students(students_data)    

# Function to add new courses (Crud - Create)
# Parameters
# - student_id, new_courses
def add_new_courses(student_id, new_courses):
    try:
        # Validate the student_id
        validate_student_id(student_id, for_student=True)
    except InvalidIDException as e:
        print(f"Error: {e}")
    except DuplicateIDException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}") 

    # Load students
    students_data = load_students()

    # Flag to track if student to be updated found
    # Loop through each student till desired student found
    student_found = False
    for student in students_data:
        if student.get_student_id() == student_id:
            student_found = True
            
            # if new courses is not none add the new courses 
            if new_courses:
                student.add_courses(new_courses)
            else:
                print("Error: No courses to add")
            break

    if not student_found:
        print(f"Error: Student with ID {student_id} not found.")
        return

    save_students(students_data)    

# Function to add new minors for undergrads (Crud - Create)
# Parameters
# - student_id, new_minors
def add_new_minors(student_id, new_minors):
    try:
        # Validate the student_id
        validate_student_id(student_id, for_minors=True)
    except InvalidIDException as e:
        print(f"Error: {e}")
    except DuplicateIDException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}") 

    students_data = load_students()

    # Flag to track if student to be updated found
    # Loop through each student till desired student found
    student_found = False
    for student in students_data:
        if student.get_student_id() == student_id:
            student_found = True
            
            # if the instance of the student is of the Undergraduate class then only proceed to add the new minors
            if isinstance(student, Undergraduate):
                # if new mionrs is not none add the new minors 
                if new_minors:
                    student.add_minors(new_minors)
                else:
                    print("Error: No minors to add")
            else:
                print(f"Error: Student with ID {student_id} is not an undergradute. Cannot add minors.")
            break
    if not student_found:
        print(f"Error: Student with ID {student_id} not found.")
        return

    save_students(students_data) 

# Function to remove a course - (cruD - Deletion)
# Parameters:
# - student_id, remove_this_course 
def remove_course(student_id, remove_this_course):
    try:
        # Validate the student id
        validate_student_id(student_id, for_student=True)
    except InvalidIDException as e:
        print(f"Error: {e}")
    except DuplicateIDException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}") 

    students_data = load_students()

    # Flag to track if student to be updated found
    # Loop through each student till desired student found
    student_found = False
    for student in students_data:
        if student.get_student_id() == student_id:
            student_found = True
            
            # if the course to be removed is not none, then remove the course
            if remove_this_course:
                student.remove_course(remove_this_course)
                break
            else:
                print(f"Error: error removing {remove_this_course}. Try again.")
                return

    if not student_found:
        print(f"Error: Student with ID {student_id} not found.")
        return

    save_students(students_data)

# Function to remove a mionr - (cruD - Deletion)
# Parameters:
# - student_id, remove_this_minor 
def remove_minor(student_id, remove_this_minor):
    try:
        # Validate the student id
        validate_student_id(student_id, for_minors=True)
    except InvalidIDException as e:
        print(f"Error: {e}")
    except DuplicateIDException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}") 

    students_data = load_students()

    # Flag to track if student to be updated found
    # Loop through each student till desired student found
    student_found = False
    for student in students_data:
        if student.get_student_id() == student_id:
            student_found = True
            # if the instance of the student is of the Undergraduate class then only proceed to remove the minor
            if isinstance(student, Undergraduate):
                # if the mionr to be removed is not none, then remove the minor
                if remove_this_minor:
                    student.remove_minor(remove_this_minor)
                    return
                else:
                    print(f"Error: error removing {remove_this_minor}. Try again.")
                    return
            else:
                print(f"Error: Student with ID {student_id} is not an undergradute. Cannot add minors.")
                return
        
    if not student_found:
        print(f"Error: Student with ID {student_id} not found.")
        return

    save_students(students_data)

# Function to delete a student - (cruD - Deletion)
# Parameter:
# - student_id
def del_student(student_id):
    try:
        # Validate student ID
        validate_student_id(student_id, for_deletion=True)
    except InvalidIDException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Load students
    students_data = load_students()

    # Flag to track if student to be deleted found
    student_found = False
    # Final check is just a second verification if the user really wants to delete a student
    final_check = ""

    # For this for loop
    # i, refers to index of a student
    # student, refers to the student object itself
    for i, student in enumerate(students_data):
        if student.get_student_id() == student_id:
            student_found = True

            # Final verification
            final_check = input(f"\nFINAL WARNING:\nAre you sure you want to delete student with ID: {student_id}? (y/n) ")
            if final_check.strip().lower() == "y":
                # Remove student through passing index
                del students_data[i]
                break
            else:
                print(f"Student with ID {student_id} not deleted")
                break
    
    if not student_found:
        print(f"Error: Student with ID {student_id} not found")

    # Save the student data 
    if final_check == "y":
        try:
            save_students(students_data)
            print(f"Student with ID {student_id} has been deleted")
        except Exception as e:
            print(f"Error writing to file {e}")
        


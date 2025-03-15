import json
from models.student import Student
from models.student import StudentEncoder
from models.student import StudentDecoder

def validate_student_id():
    pass

def add_student(student_id, name, age, courses):
    try:
        with open("student_management/students.json", "r") as f:
            students_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        students_data = [] # IF the file does not exist or is empty, start with an empty list

    if any(s['student_id'] == student_id for s in students_data):
        print(f"Error: Student with ID {student_id} already exists.")
        return
    else:
        new_student = Student(student_id, name, age, courses)
        students_data.append(new_student)

    with open("student_management/students.json", "w") as f:
        json.dump(students_data, f, cls=StudentEncoder, indent=4)

    print(f"Student {student_id} has been added successfully!")

def list_all_students():
    try:
        with open("student_management/students.json", "r") as f:
            students_data = json.load(f, cls=StudentDecoder)
    except (FileNotFoundError, json.JSONDecodeError):
        students_data = [] # IF the file does not exist or is empty, start with an empty list

    for i in students_data:
        print(i)

def update_student(student_id, new_name=None, new_age=None, old_course=None, new_course=None):
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

            if new_name:
                student.update_name(new_name)
            if new_age:
                student.update_age(new_age) 
            if old_course and new_course:
                student.update_courses(old_course, new_course)
            print(f"Student {student_id} updated successfully!")
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
    

def del_student(student_id):
    try:
        with open("student_management/students.json", "r") as f:
            students_data = json.load(f, cls=StudentDecoder)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No students found.")
        return

    student_found = False

    for i, student in enumerate(students_data):
        if student.get_student_id() == student_id:
            student_found = True
            del students_data[i]
            break

    
    if not student_found:
        print(f"Error: Student with ID {student_id} not found")
        return

    try:
        with open("student_management/students.json", "w") as f:
            json.dump(students_data, f, indent=4, cls=StudentEncoder)
        print(f"Student with ID {student_id} has been deleted")
    except Exception as e:
        print(f"Error writing to file {e}")
    
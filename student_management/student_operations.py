import json
from models.student import Student
from models.student import StudentEncoder

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
            students_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        students_data = [] # IF the file does not exist or is empty, start with an empty list

    for student in students:
        print(student.get_student_details())
        print("-" * 30)

def update_student(student_id, new_name=None, new_age=None, new_courses=None):
    student = next((s for s in students if s.get_student_id() == student_id), None)

    if student:
        if new_name:
            student.update_name(new_name)
        if new_age:
            student.update_age(new_age)
        if new_courses:
            student.update_course(new_courses)
        print(f"Student {student_id} updated successfully!")
    else:
        print(f"Error: Student with ID {student_id} not found.")

def del_student(student_id):
    global students
    students = [s for s in students if s.get_student_id() != student_id]
    
    print(f"Student(s) with ID {student_id} has been deleted")

from student_operations import *

def display_menu():
    print("Student Management System")
    print("1. Add a student")
    print("2. Update a student")
    print("3. Delete a student")
    print("4. View all students")
    print("5. Exit")

def main():
    while True:
        display_menu()

        choice = int(input("Choose an option: "))

        if choice == 1:
            try: 
                student_id = int(input("Enter the student ID (6 digits minimum): "))
                student_name = input("Enter the student name: ")
                student_age = int(input("Enter the student age: "))
                undergrad = input("Is the student an undergrad with a minor (y/n): ")
                if undergrad.lower().strip() == "y":
                    minors_inputs = input("Enter the student's minor/s (separated by commans if more than 1 minor): ")
                minors = [minor for minor in minors_inputs.split(",")]
                courses_inputs = input("Enter the course(s) (separated by commas if more than 1 course): ")
                courses = [course.strip() for course in courses_inputs.split(",")]

                validate_student_id(student_id)

                if undergrad.lower().strip() == "y":
                    add_student(student_id, student_name, student_age, courses, True, minors)
                else:
                    add_student(student_id, student_name, student_age, courses, False, None)
            except InvalidIDException as e:
                print(f"Error: {e}")
            except DuplicateIDExcption as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}") 

        elif choice == 2:
            try:
                student_id = int(input("Enter the student ID (6 digits minimum): "))
                student_name = input("Enter the student name: ")
                student_age = int(input("Enter the student age: "))
                course_to_update = input("Enter the course to update: ")
                new_course = input("Enter the new course: ")
                update_student(student_id, student_name, student_age, course_to_update, new_course)
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == 3:
            student_id = int(input("Enter the student ID to delete (6 digits minimum): "))
            try:
                validate_student_id(student_id)
                del_student(student_id)
            except InvalidIDException as e:
                print(f"Error: {e}")
            except DuplicateIDExcption as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}") 
        
        elif choice == 4:
            list_all_students()
        
        elif choice == 5:
            break

if __name__ == "__main__":
    main()
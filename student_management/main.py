from student_operations import *
import time

def display_menu():
    time.sleep(1)
    print("\nStudent Management System")
    print("1. Add a student")
    print("2. Update a student")
    print("3. Delete a student")
    print("4. View all students")
    print("5. Exit")

def main():
    while True:
        display_menu()

        choice = int(input("Choose an option: "))
        if choice == 5:
            break
        print(f"Loading your option {choice}")
        time.sleep(1.2)

        if choice == 1:
            try: 
                student_id = int(input("Enter the student ID (6 digits minimum): "))
                validate_student_id(student_id, for_student=True)
                student_name = input("Enter the student name: ")
                student_age = int(input("Enter the student age: "))
                undergrad = input("Is the student an undergrad with a minor (y/n): ")
                if undergrad.lower().strip() == "y":
                    minors_inputs = input("Enter the student's minor/s (separated by commans if more than 1 minor): ")
                    minors = [minor for minor in minors_inputs.split(",")]
                courses_inputs = input("Enter the course(s) (separated by commas if more than 1 course): ")
                courses = [course.strip() for course in courses_inputs.split(",")]

                # validate_student_id(student_id)

                if undergrad.lower().strip() == "y":
                    add_student(student_id, student_name, student_age, courses, True, minors)
                else:
                    add_student(student_id, student_name, student_age, courses, False, None)
            except InvalidIDException as e:
                print(f"Error: {e}")
            except DuplicateIDException as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}") 

        elif choice == 2:
            try:
                student_id = int(input("Enter the student ID (6 digits minimum) to update the student: "))

                print(f"\nStudent Details for ID: {student_id}")
                list_a_student(student_id)  
                time.sleep(1.2)

                print("\nOptions for updating students: ")
                print("1. Student Name")
                print("2. Student Age")
                print("3. Replace an Existing Course")
                print("4. Add New Courses")
                print("5. Remove a Course")
                print("6. Update Minors")
                print("7. Add New Minors")
                print("8. Remove a Minor")
                print("9. Back to Menu")


                
                update_choice = int(input("Enter your choice (1-9): "))

                if update_choice == 1:
                    new_name = input("Enter new name: ").strip()
                    update_student(student_id, new_name=new_name)
                    time.sleep(1.2)
                elif update_choice == 2:
                    new_age = int(input("Enter new age: "))
                    update_student(student_id, new_age=new_age)
                    time.sleep(1.2)

                elif update_choice == 3:
                    old_course = input("Enter the course to replace: ").strip()
                    new_course = input("Enter the new course: ").strip()
                    update_student(student_id, old_course=old_course, new_course=new_course)
                    time.sleep(1.2)

                elif update_choice == 4:
                    new_courses_input = input("Enter new courses (comma-separated): ")
                    new_courses = [course.strip() for course in new_courses_input.split(",")]
                    add_new_courses(student_id, new_courses)
                    time.sleep(1.2)

                elif update_choice == 5:
                    remove_this_course = input("Enter the course to remove: ").strip()
                    remove_course(student_id, remove_this_course)
                    time.sleep(1.2)
                
                elif update_choice == 6:
                    new_minors_input = input("Enter new minors (comma-separated): ")
                    new_minors = [course.strip() for course in new_minors_input.split(",")]
                    update_student(student_id, minors=new_minors)
                    time.sleep(1.2)
                            
                elif update_choice == 7:
                    new_minors_input = input("Enter new minors (comma-separated): ")
                    new_minors = [course.strip() for course in new_minors_input.split(",")]
                    add_new_minors(student_id, new_minors)
                    time.sleep(1.2)
                elif update_choice == 8:
                    remove_this_minor = input("Enter the minor to remove: ").strip()
                    remove_minor(student_id, remove_this_minor)
                    time.sleep(1.2)
                elif update_choice == 9:
                    continue

                else:
                    print("Invalid choice. Please enter a valid option")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == 3:
            student_id = int(input("Enter the student ID to delete (6 digits minimum): "))
            try:
                validate_student_id(student_id, True)
                del_student(student_id)
            except InvalidIDException as e:
                print(f"Error: {e}")
            except DuplicateIDException as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}") 
        
        elif choice == 4:
            list_all_students()
        
        else:
            print("\nInvalid option.")

if __name__ == "__main__":
    main()
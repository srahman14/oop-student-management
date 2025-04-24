from student_operations import *
import time

# Display menu options
def display_menu():
    time.sleep(1)
    # Menu options
    print("\nStudent Management System")
    print("1. Add a student")
    print("2. Update a student")
    print("3. Delete a student")
    print("4. View all students")
    print("5. Exit")

# Main functionality of program
def main():
    while True:
        display_menu()

        # Menu choice 1-5
        choice = int(input("Choose an option: "))

        # Place choice 5 here so the program doesn't have to traverse through all the if statements just to exit
        if choice == 5:
            break

        print(f"Loading your option {choice}")
        time.sleep(1.2)

        # Add a student
        if choice == 1:
            try: 
                # The reason I have impleneted this method to attain the ID is because by default leading zeros 
                # in an integer are not preserved in Python. So I take the input as a string first, 
                # then convert it into an integer with enforcing a rule that all IDs must not begin with 0.
                raw_id = input("Enter the student ID (6 digits minimum, cannot start with 0): ").strip()

                if raw_id.startswith("0"):
                    print("Error: Student ID cannot start with 0")
                    continue
                if not raw_id.isdigit():
                    print("Error: Student ID must contain only digits.")
                    continue
                
                student_id = int(raw_id)
                # Validate the student ID before continuing with attaining the rest of the variables to save time
                # from an invalid student ID
                validate_student_id(student_id)
                # Get all required variables needed to pass into our add_student function
                student_name = input("Enter the student name: ")
                student_age = int(input("Enter the student age: "))
                undergrad = input("Is the student an undergrad with a minor (y/n): ")
                # Verify if the student is an undergrad for adding minors
                if undergrad.lower().strip() == "y":
                    minors_inputs = input("Enter the student's minor/s (separated by commas if more than 1 minor): ")
                    # Use .split() to take all inputs separated by commas and store them in a list
                    minors = [minor for minor in minors_inputs.split(",")]
                courses_inputs = input("Enter the course(s) (separated by commas if more than 1 course): ")
                # Use .split() to take all inputs separated by commas and store them in a list
                courses = [course.strip() for course in courses_inputs.split(",")]

                # If student is an undergrad, 'undergrad' is set to True to ensure the Undergraduate class is used
                # else the normal student class is used
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

        # Update a student
        elif choice == 2:
            try:
                raw_id = input("Enter the student ID to update (6 digits minimum, cannot start with 0): ").strip()

                if raw_id.startswith("0"):
                    print("Error: Student ID cannot start with 0")
                    continue
                if not raw_id.isdigit():
                    print("Error: Student ID must contain only digits.")
                    continue
                
                student_id = int(raw_id)
                validate_student_id(student_id, for_updating=True)

                print(f"\nStudent Details for ID: {student_id}")
                list_a_student(student_id)  
                time.sleep(1.4)

                # All options related to updating a student
                print("\nOptions for updating students: ")
                print("1. Student Name")
                print("2. Student Age")
                print("3. Replace an Existing Course")
                print("4. Add New Courses")
                print("5. Remove a Course")
                print("6. Add New Minors")
                print("7. Remove a Minor")
                print("8. Back to Menu")

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
                    # Use .split() to take all inputs separated by commas and store them in a list
                    new_courses = [course.strip() for course in new_courses_input.split(",")]
                    add_new_courses(student_id, new_courses)
                    time.sleep(1.2)

                elif update_choice == 5:
                    remove_this_course = input("Enter the course to remove: ").strip()
                    remove_course(student_id, remove_this_course)
                    time.sleep(1.2)
                            
                elif update_choice == 6:
                    new_minors_input = input("Enter new minors to add on to existing minors (comma-separated): ")
                    # Use .split() to take all inputs separated by commas and store them in a list
                    new_minors = [course.strip() for course in new_minors_input.split(",")]
                    add_new_minors(student_id, new_minors)
                    time.sleep(1.2)

                elif update_choice == 7:
                    remove_this_minor = input("Enter the minor to remove: ").strip()
                    remove_minor(student_id, remove_this_minor)
                    time.sleep(1.2)
                elif update_choice == 8:
                    continue

                else:
                    print("Invalid choice. Please enter a valid option")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")
        
        # Delete Student
        elif choice == 3:
            raw_id = input("Enter the student ID to update (6 digits minimum, cannot start with 0): ").strip()

            if raw_id.startswith("0"):
                print("Error: Student ID cannot start with 0")
                continue
            if not raw_id.isdigit():
                print("Error: Student ID must contain only digits.")
                continue

            student_id = int(raw_id)
            try:
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
"""
student.py
----------
Defines the core `Student` class for the Student Management System.

Implements encapsulation by using private attributes and providing
getter and setter methods. Includes course management features and
student detail retrieval methods.

Part of Task 1: Implement Student Class with Encapsulation.
"""

import time

class Student:
    def __init__(self, student_id, name, age, courses):
        # Private attributes
        self.__student_id = student_id
        self.__name = name
        self.__age = age
        self.__courses = courses

    # Setter function for student ID
    def set_student_id(self, setID: int):
        # If the student ID is none/zero/non-integer then return as student ID is invalid
        if setID is None:
            print(f"Error: {setID} is not a valid input. Input must be a positive integer.")
            return
        if not isinstance(setID, int) or setID <= 0:
            print(f"Error: {setID} is not a valid input. Input must be a positive integer.")
            return
        
        # Else set the student ID
        self.__student_id = setID 
        print(f"Student ID has been updated to: ", self.__student_id)

    # Getter methods for:
    # - returning student ID
    # - returning student details
    # - returning student name
    # - returning student age
    # - returning student courses

    def get_student_id(self):
        # Verify the student ID, as a student ID could be unset 
        if self.__student_id is None or self.__student_id == 0:
            print("Student ID is not set. Please set ID first.")
            print("Use: set_student_id('STUDENT_ID_HERE') to set an ID")
            return

        return self.__student_id

    # Return all student details
    def get_student_details(self):
        return f"Student ID: {self.__student_id}\nStudent Name: {self.__name}\nStudent Age: {self.__age}\nStudent Course(s): {self.__courses}"
    
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_courses(self):
        return self.__courses
    
    def get_minor(self):
        # This will return an empty list if no minors are assigned, or minors from the subclass
        if hasattr(self, '_Undergraduate__minors'):  # Check if minor attribute exists
            return getattr(self, '_Undergraduate__minors')
        # No minors in base Student class, default
        return []  


    # Update courses method - this takes two parameters
    # - old_course - the course to be replaced
    # - new_course - the course to replace the old course
    def update_courses(self, old_course: str, new_course: str):
        # normalised_courses - list which converts all the current courses with all the inital letters 
        # of every course capitalised. This is useful when I do checking for the old_course/new_course 
        # if they already exist etc. This is just a standardised way for me to verify before making any 
        # changes. 
        normalised_courses = [course.lower().capitalize() for course in self.__courses]

        if old_course.lower().capitalize() not in normalised_courses:
            print(f"\nCourse '{old_course}' does not exist")
            print(f"\nStudent '{self.__name}' Current Enrollment:\nStudent Course(s): {self.__courses}\n")
            return
        
        if new_course.lower().capitalize() in normalised_courses:
            print(f"\nCourse '{new_course}' already exists")
            return
        
        # Use of try-catch for efficient error-handling
        try:
            # Attain the index of the course to be changed and replace the old_course through referencing
            # the index of the old_course and assign it to the new course
            index = normalised_courses.index(old_course.lower().capitalize().strip())
            self.__courses[index] = new_course.lower().capitalize().strip()
            print("Updating courses...")
            time.sleep(2)
            print(f"\nUpdated Course(s): [{', '.join(self.__courses)}]")
        except ValueError as e:
            print(f"Error updating course: {e}")
    
    def update_name(self, new_name: str):
        # Both 'numbers' and 'symbols' are lists to verify a user's input for their name does not contain any
        # numbers or special characters

        # Numbers 1-10
        numbers = [str(number) for number in range(0,10)]

        # Use set to wrap string in three quotes to handle single/double quotes
        # Use of 'r' in front to handle escape character
        # set converts the string to a set
        symbols = set(r"""`~!@#$%^&*()_-+={[}}|\:;"'<,>.?/""")

        # If the name is less than two characters, return back to the main menu
        if len(new_name) < 2:
            print("This name is too short, must be at least 2-3 characters minimum. Try again.\n") 
            return
        
        # Verify if the name contains any symbols or numbers
        if any(symbol in new_name for symbol in symbols):
            print("You cannot use any special characters. Try again.\n")
            return

        if any(number in new_name for number in numbers):
            print("You cannot use any numbers. Try again.\n")
            return
        
        self.__name = new_name
            
    
    def update_age(self, age: int):
        # Ensure the age is at least 2 or 3 digits
        if len(str(age)) <= 1 or len(str(age)) > 3: 
            print("Update Age:\n- Age must be 2 digits minimum\n- Age cannot be more than 3 digits long\n") 
        # Ensure the age is nonzero
        if age == 0:
            print("Update Age:\n- Age cannot be 0\n") 
        # Ensure the age input is an integer
        if type(age) != int:
            print("Only numbers accepted for updating age")
            return

        self.__age = age

    # Method for adding MULTIPLE courses. This differs from the update_course method, as this method is to add
    # courses, and not replace any courses. new_courses is defined as any, as it could be just one input or a list
    def add_courses(self, new_courses: list):
        # Similar to aforementioned 'normalised_courses', 'new_courses' is just all the new courses the user
        # wishes to add with all the courses capitalised to avoid a user from bypassing the system to add an
        # existing course.
        new_courses = [course.lower().capitalize() for course in new_courses]
        noramlised_courses = [course.lower().capitalize() for course in self.__courses]

        # Verify if a course already exists, else add it to the user's courses
        for new_course in new_courses:
            if new_course in noramlised_courses:
                print(f"Error: Course '{new_course}' already exists")
            else:
                self.__courses.append(new_course)
                print(f"Added: Course '{new_course}' added for {self.__name}, ID: {self.__student_id}")
        
        print(f"\nUpdated Course(s):\n {', '.join(self.__courses)}")

    def remove_course(self, remove_course: str):
        # If no courses exist, return to main menu (base case)
        if len(self.__courses) == 0:
            print(f"Error: Cannot remove courses from a student with no courses")
            return
        # Check if the course user wishes to remove exists - if so remove this course
        if remove_course not in self.__courses:
            print(f"Error: Course '{remove_course}' does not exist for student {self.__name} with ID: {self.__student_id}")
            return
        else:
            self.__courses.remove(remove_course)
            print(f"Removed: Course '{remove_course}' for {self.__name}, ID: {self.__student_id}")
    
        print(f"\nUpdated Course(s):\n {', '.join(self.__courses)}")

    # Displaying the object in desired and formatted way
    def __str__(self):
        # Formatting for courses and minors to be on new lines with dashes
        courses_str = "\n - ".join(self.get_courses())
        minors_str = "\n - ".join(self.get_minor()) if self.get_minor() else "No minors assigned."
        
        return (f"Student ID: {self.get_student_id()}\n"
                f"Student Name: {self.get_name()}\n"
                f"Student Age: {self.get_age()}\n"
                f"Student Courses:\n - {courses_str}\n"
                f"Student Minors: \n - {minors_str}\n"
                f"---------------------------------------------------------------------------")

    # Useful for debugging
    def __repr__(self):
        return (f"Student(student_id={self.get_student_id()}, "
                f"name={self.get_name()}, age={self.get_age()}, "
                f"courses={self.get_courses()}, minors={self.get_minor()})")    
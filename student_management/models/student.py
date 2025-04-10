import time

class Student:
    def __init__(self, student_id, name, age, courses):
        # Private attributes
        self.__student_id = student_id
        self.__name = name
        self.__age = age
        self.__courses = courses

    def set_student_id(self, setID: int):
        # Verify the ID is not none
        if setID is None:
            print(f"Error: {setID} is not a valid input. Input must be a positive integer.")
            return
        # Verify the ID is an integer and not less than 0
        if not isinstance(setID, int) or setID <= 0:
            print(f"Error: {setID} is not a valid input. Input must be a positive integer.")
            return
        # Set student ID
        self.__student_id = setID 
        print(f"Student ID has been updated to: ", self.__student_id)

 
    def get_student_id(self):
        # Verify the student ID is set
        if self.__student_id is None or self.__student_id == 0:
            print("Student ID is not set. Please set ID first.")
            return

        return self.__student_id

    # Return all information for student ID
    def get_student_details(self):
        return f"Student ID: {self.__student_id}\nStudent Name: {self.__name}\nStudent Age: {self.__age}\nStudent Course(s): {self.__courses}"
    
    def update_courses(self, old_course, new_course):
        # Normalised Courses is just a list holding all the courses of the student capitalised
        normalised_courses = [course.capitalize() for course in self.__courses]

        # Check if the 'old_course' (course to be replaced) does not exists in the current courses
        if old_course.capitalize() not in normalised_courses:
            print(f"\nCourse '{old_course}' does not exist")
            print(f"\nStudent '{self.__name}' Current Enrollment:\nStudent Course(s): {self.__courses}\n")
            return
        
        # Check if the 'new_course' already exists in the current courses
        if new_course.capitalize() in normalised_courses:
            print(f"\nCourse '{new_course}' already exists")
            return
        
        try:
            # Get the index of the old course from normalised courses, as normalised courses is a temporary clean version of
            # self.__courses. It is a safer way to find index (even if the original has abnormal capitalisation)
            index = normalised_courses.index(old_course.capitalize().strip())
            self.__courses[index] = new_course.capitalize().strip()
            print("Updating courses...")
            time.sleep(2)
            print(f"\nUpdated Course(s): [{', '.join(self.__courses)}]")
        except ValueError as e:
            print(f"Error updating course: {e}")
    
    def update_name(self, newName: str):
        # print("Update Name:\n- Name must be 2-3 characters minimum\n- Do not include any special characters\n- Do not include any numbers\n") 
        numbers = [str(number) for number in range(0,10)]

        # Use set to wrap string in three quotes to handle single/double quotes
        # Use of 'r' in front to handle escape character
        # set converts the string to a set
        symbols = set(r"""`~!@#$%^&*()_-+={[}}|\:;"'<,>.?/""")

        # Verify length of name
        if len(newName) < 2:
            print("This name is too short, must be at least 2-3 characters minimum. Try again.\n") 
            return
        # Verify if any symbols in name
        if any(symbol in newName for symbol in symbols):
            print("You cannot use any special characters. Try again.\n")
            return
        # Verify if any numbers in name
        if any(number in newName for number in numbers):
            print("You cannot use any numbers. Try again.\n")
            return
        
        # Update name
        self.__name = newName
            
    
    def update_age(self, age: int):
        # Verify age is nonzero
        if age == 0:
            print("Update Age:\n- Age cannot be 0\n") 
        # Verify length of age input
        if len(str(age)) <= 1 or len(str(age)) > 3: 
            print("Update Age:\n- Age must be 2 digits minimum\n- Age cannot be more than 3 digits long\n") 
        # Verify age is an integer
        if type(age) != int:
            print("Only numbers accepted for updating age")
            return
        # If all cases pass, update age
        self.__age = age

    def add_courses(self, new_courses):
        # New Courses is just a list holding all the 'new_courses' capitalised
        new_courses = [course.capitalize() for course in new_courses]

        for new_course in new_courses:
            # Check if new course already exists
            if new_course in self.__courses:
                print(f"Error: Course '{new_course}' already exists")
            else:
                # If not, add the new courses to the existing courses of student
                self.__courses.append(new_course)
                print(f"Added: Course '{new_course}' added for {self.__name}, ID: {self.__student_id}")
        
        print(f"\nUpdated Course(s):\n {', '.join(self.__courses)}")

    def remove_course(self, remove_course):
        # Verify a student has any courses to begin with
        if len(self.__courses) == 0:
            print(f"Error: Cannot remove courses from a student with no courses")
            return
        # Verify the course the user wants to remove exists
        if remove_course not in self.__courses:
            print(f"Error: Course '{remove_course}' does not exist for student {self.__name} with ID: {self.__student_id}")
            return
        else:
            # Remove the course
            self.__courses.remove(remove_course)
            print(f"Removed: Course '{remove_course}' for {self.__name}, ID: {self.__student_id}")
    
        print(f"\nUpdated Course(s):\n {', '.join(self.__courses)}")

    # Getters
    def get_student_id(self):
        return self.__student_id

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

    # Useful for when object is printed
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
import time

class Student:
    def __init__(self, student_id, name, age, courses):
        self.__student_id = student_id
        self.__name = name
        self.__age = age
        self.__courses = courses

    def set_student_id(self, setID: int):
        if setID is None:
            print(f"Error: {setID} is not a valid input. Input must be a positive integer.")
            return
        if not isinstance(setID, int) or setID <= 0:
            print(f"Error: {setID} is not a valid input. Input must be a positive integer.")
            return
        
        self.__student_id = setID 
        print(f"Student ID has been updated to: ", self.__student_id)

 
    def get_student_id(self):
        if self.__student_id is None or self.__student_id == 0:
            print("Student ID is not set. Please set ID first.")
            print("Use: set_student_id('STUDENT_ID_HERE') to set an ID")
            return

        return self.__student_id

    def get_student_details(self):
        return f"Student ID: {self.__student_id}\nStudent Name: {self.__name}\nStudent Age: {self.__age}\nStudent Course(s): {self.__courses}"
    
    def update_courses(self, old_course, new_course):
        normalised_courses = [course.capitalize() for course in self.__courses]

        if old_course.capitalize() not in normalised_courses:
            print(f"\nCourse '{old_course}' does not exist")
            print(f"\nStudent '{self.__name}' Current Enrollment:\nStudent Course(s): {self.__courses}\n")
            return
        
        if new_course.capitalize() in normalised_courses:
            print(f"\nCourse '{new_course}' already exists")
            return
        
        try:
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

        
        if len(newName) < 2:
            print("This name is too short, must be at least 2-3 characters minimum. Try again.\n") 
            return
        
        if any(symbol in newName for symbol in symbols):
            print("You cannot use any special characters. Try again.\n")
            return

        if any(number in newName for number in numbers):
            print("You cannot use any numbers. Try again.\n")
            return
        
        self.__name = newName
            
    
    def update_age(self, age: int):
        if len(str(age)) <= 1 or len(str(age)) > 3: 
            print("Update Age:\n- Age must be 2 digits minimum\n- Age cannot be more than 3 digits long\n") 
        if age == 0:
            print("Update Age:\n- Age cannot be 0\n") 
        if type(age) != int:
            print("Only numbers accepted for updating age")
            return

        self.__age = age

    def add_courses(self, new_courses):
        new_courses = [course.capitalize() for course in new_courses]

        for new_course in new_courses:
            if new_course in self.__courses:
                print(f"Error: Course '{new_course}' already exists")
            else:
                self.__courses.append(new_course)
                print(f"Added: Course '{new_course}' added for {self.__name}, ID: {self.__student_id}")
        
        print(f"\nUpdated Course(s):\n {', '.join(self.__courses)}")

    def remove_course(self, remove_course):
        if len(self.__courses) == 0:
            print(f"Error: Cannot remove courses from a student with no courses")
            return
        if remove_course not in self.__courses:
            print(f"Error: Course '{remove_course}' does not exist for student {self.__name} with ID: {self.__student_id}")
            return
        else:
            self.__courses.remove(remove_course)
            print(f"Removed: Course '{remove_course}' for {self.__name}, ID: {self.__student_id}")
    
        print(f"\nUpdated Course(s):\n {', '.join(self.__courses)}")

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_courses(self):
        return self.__courses

    # Useful for when object is printed
    def __str__(self):
        courses_str = "\n - ".join(self.get_courses())
        return (f"Student ID: {self.get_student_id()}\n"
                f"Student Name: {self.get_name()}\n"
                f"Student Age: {self.get_age()}\n"
                f"Student Courses:\n - {courses_str}\n"
                f"---------------------------------------------------------------------------")

    # Useful for debugging
    def __repr__(self):
        return f"Student(student_id={self.get_student_id()}, name={self.get_name()}, age={self.get_age()}, courses={self.get_courses()})"
        


# john = Student(0(), "John", 18, ["History", "Spanish", "Maths"])
# john.get_student_details()
# john.set_student_id()

# john.updateCourse()
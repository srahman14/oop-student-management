import time
import json

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
            return

        return self.__student_id

    def get_student_details(self):
        return f"Student ID: {self.__student_id}\nStudent Name: {self.__name}\nStudent Age: {self.__age}\nStudent Course(s): {self.__courses}"
    
    def update_course(self):
        changeCourse = input("Enter the course to change: ").strip().capitalize()

        normalised_courses = [course.capitalize() for course in self.__courses]

        while True:
            changeCourse = input("Enter the course to change: ").strip().capitalize()

            if changeCourse in normalised_courses:
                break
            print(f"\nCourse '{changeCourse}' does not exist")
            print(f"Current Enrollment:\nStudent Course(s): {self.__courses}\n")

        while True:
            newCourse = input("Enter the new course: ").capitalize()

            if not newCourse:
                print("Error: Course name cannot be empty")
                continue
            
            if newCourse in normalised_courses:
                print(f"Error: Course {newCourse} already exists")
                continue
            
            if newCourse not in normalised_courses:
                break
        try:
            if changeCourse.strip() in self.__courses:
                index = normalised_courses.index(changeCourse)
                self.__courses[index] = newCourse

                print("Updating courses...")
                time.sleep(3)

                print(f"\nUpdated Courses: [{', '.join(self.__courses)}]")
        except ValueError as e:
            print(f"Error updating course: {e}")
    
    def update_name(self, newName: str):
        print("Update Name:\n- Name must be 2-3 characters minimum\n- Do not include any special characters\n- Do not include any numbers\n") 
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
        print("Update Age:\n- Age must be 1 character minimum\n") 
    
        if type(age) != int:
            print("Only numbers accepted for updating age")
            return

        self.__age = age
    
    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_courses(self):
        return self.__courses

class StudentEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Student):
            return {"student_id": o.get_student_id(), "name": o.get_name(), "age": o.get_age(), "courses": o.get_courses()}
        
        return super().default(o)

        

# john = Student(0(), "John", 18, ["History", "Spanish", "Maths"])
# john.get_student_details()
# john.set_student_id()

# john.updateCourse()
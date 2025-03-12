import time
import os # will use to write errors to log.txt

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

        return f"ID for student {self.__name}: {self.__student_id}"

    def get_student_details(self):
        return f"Student ID: {self.__student_id}\nStudent Name: {self.__name}\nStudent Age: {self.__age}\nStudent Course(s): {self.__courses}"
    
    def updateCourse(self):
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
            

# john = Student(0, "John", 18, ["History", "Spanish", "Maths"])
# john.get_student_details()
# john.set_student_id()

# john.updateCourse()
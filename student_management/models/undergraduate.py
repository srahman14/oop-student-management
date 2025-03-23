from models.student import Student

class Undergraduate(Student):
    def __init__(self, student_id, name, age, courses, minor: list):
        super().__init__(student_id, name, age, courses)

        self.__minors = minor
    
    def get_details(self):
        existing_details = super().get_student_details() 
        return f"{existing_details}\nMinor: {self.__minors}"

    def get_minor(self):
        return self.__minors
    
    def update_minors(self, new_minors):
        if not new_minors:
            print("Error: No minors provided for update.")
            return

        self.__minors = new_minors
        print("Minor(s) updated successfully")
        print(f"\nUpdated Minor(s):\n {', '.join(self.__minors)}")

    
    def add_minors(self, new_minors):
        new_minors = [course.capitalize() for course in new_minors]

        for new_course in new_minors:
            if new_course in self.__minors:
                print(f"Error: Course '{new_course}' already exists")
                return
            elif new_course not in self.__minors:
                self.__minors.append(new_course)
                print(f"Added: Course '{new_course}' added for {self.__name}, ID: {self.__student_id}")
   

        print(f"\nUpdated Minor(s):\n {', '.join(self.__minors)}")

    def remove_minor(self, remove_minor):
        if len(self.__minors) == 0:
            print(f"Error: Cannot remove minors from a student with no minors")
            return
        if remove_minor not in self.__minors:
            print(f"Error: minor '{remove_minor}' does not exist for student {self.__name} with ID: {self.__student_id}")
            return
        else:
            self.__minors.remove(remove_minor)
            print(f"Removed: minor '{remove_minor}' for {self.__name}, ID: {self.__student_id}")
    
        print(f"\nUpdated minor(s):\n {', '.join(self.__minors)}")


# john = Undergraduate(101, "John Doe", 20, ["CS", "AI"], "Mathematics")
# print(john.get_details())
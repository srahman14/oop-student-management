from student import Student

class Undergraduate(Student):
    def __init__(self, student_id, name, age, courses, minor):
        super().__init__(student_id, name, age, courses)

        self.__minor = minor
    
    def get_details(self):
        existing_details = super().get_student_details() 
        return f"{existing_details}\nMinor: {self.__minor}"


john = Undergraduate(101, "John Doe", 20, ["CS", "AI"], "Mathematics")
print(john.get_details())
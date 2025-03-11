class Student:
    def __init__(self, student_id, name, age, *courses):
        self.__student_id = student_id
        self.name = name
        self.age = age
        self.courses = courses

    def set_student_id(self):
        try:
            setID = int(input("Set student ID: "))

            # If the student ID is not set, it's None, so using not helps set the ID 
            if not self.__student_id:
                self.__student_id = setID 
        except ValueError:
            print("To set an ID, input should only consist of intergers.")
    def get_student_id(self):
        try:
            if self.__student_id != 0 or self.__student_id != None:
                return f"ID for student {self.name}: ", self.__student_id
        except ValueError:
            print("ID is not set")

john = Student(0, "John", 18, ["History", "Spanish", "Maths"])

print(john.get_student_id())



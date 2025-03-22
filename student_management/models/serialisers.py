from models.student import Student
from models.undergraduate import Undergraduate
import json

class StudentEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Student):
            if isinstance(o, Undergraduate):
                return {
                    "student_id": o.get_student_id(),
                    "name": o.get_name(),
                    "age": o.get_age(),
                    "courses": o.get_courses(),
                    "minor": o.get_minor(),
                }
            else:
                return {
                    "student_id": o.get_student_id(), 
                    "name": o.get_name(), 
                    "age": o.get_age(), 
                    "courses": o.get_courses(), 
                }
        
        return super().default(o)

class StudentDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.object_hook)

    def object_hook(self, dct):
        if "student_id" in dct and "name" in dct and "age" in dct and "courses" in dct:
            if "minor" in dct:
                return Undergraduate(dct["student_id"], dct["name"], dct["age"], dct["courses"], dct["minor"]) 
            return Student(dct["student_id"], dct["name"], dct["age"], dct["courses"])
        return dct
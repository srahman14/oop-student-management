import json
from models.serialisers import StudentEncoder, StudentDecoder

FILE_PATH = "student_management/students.json"

def load_students():
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f, cls=StudentDecoder)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] 
    
def save_students(students_data):
    try:
        with open(FILE_PATH, "w") as f:
            json.dump(students_data, f, indent=4, cls=StudentEncoder)
    except Exception as e:
        print(f"Error writing to file: {e}")
    



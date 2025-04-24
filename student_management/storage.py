"""
storage.py
----------
Handles persistent data storage and retrieval for student records.

Provides functions to save to and load from a JSON file. Converts between
student objects and dictionary representations.

Part of Task 5: Implement File Storage for Student Records.
"""

import json
from models.serialisers import StudentEncoder, StudentDecoder

# File Path for where to import/export student data from
FILE_PATH = "student_management/students.json"

# Function for loading students
def load_students():
    # Open the file and load the student data, if not found return an empty list
    try:
        with open(FILE_PATH, "r") as f:
            # Use of StudentEncoder to convert from JSON into student object
            return json.load(f, cls=StudentDecoder)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] 
    
def save_students(students_data):
    # Open the file and save the student data, if not found raise an exception
    try:
        with open(FILE_PATH, "w") as f:
            # Use of indentation and StudentEncoder to convert into JSON in desired format
            json.dump(students_data, f, indent=4, cls=StudentEncoder)
    except Exception as e:
        print(f"Error writing to file: {e}")
    



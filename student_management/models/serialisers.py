"""
serialisers.py
--------------
Provides JSON encoding and decoding logic for Student and Undergraduate objects.

This module defines custom JSONEncoder and JSONDecoder subclasses to handle
serialization (saving to JSON) and deserialization (loading from JSON) of 
Student and Undergraduate objects, preserving object structure and class hierarchy.

Used to integrate object-oriented structures with persistent file storage.

Additionally added for Part of Task 5: Implement File Storage for Student Records.
"""

from models.student import Student
from models.undergraduate import Undergraduate
import json

class StudentEncoder(json.JSONEncoder):
    # Override the default() method to define how custom Student and Undergraduate objects are serialised
    # 'o', being  the object in reference
    def default(self, o):
        # If the instance of the object is a student
        if isinstance(o, Student):
            # If the instance of the object is an undergrad encode into JSON in this format
            if isinstance(o, Undergraduate):
                return {
                    "student_id": o.get_student_id(),
                    "name": o.get_name(),
                    "age": o.get_age(),
                    "courses": o.get_courses(),
                    "minor": o.get_minor(),
                }
            # Else for student's who aren't undergrads in this format
            else:
                return {
                    "student_id": o.get_student_id(), 
                    "name": o.get_name(), 
                    "age": o.get_age(), 
                    "courses": o.get_courses(), 
                }
        
        # Fall back to the default behavior for other object types
        return super().default(o)

class StudentDecoder(json.JSONDecoder):
    def __init__(self):
        # Override the default initaliser to use a custom object_hook
        super().__init__(object_hook=self.object_hook)

    def object_hook(self, dct):
        # This method is automatically called during JSON decoding.
        # It converts JSON dictionaries into Student or Undergraduate objects,
        # based on the presence of the 'minor' key.
        if "student_id" in dct and "name" in dct and "age" in dct and "courses" in dct:
            if "minor" in dct:
                return Undergraduate(dct["student_id"], dct["name"], dct["age"], dct["courses"], dct["minor"]) 
            return Student(dct["student_id"], dct["name"], dct["age"], dct["courses"])
        return dct
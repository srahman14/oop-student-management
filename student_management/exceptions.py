"""
exceptions.py
-------------
Defines custom exception classes for validation and ID conflict handling.

Improves code clarity and robust error handling through
`InvalidIDException` and `DuplicateIDException`.

These classes inherit from the base Exception class to be able to raise an
error to avoid the program from breaking.

Part of Task 4: Implement Exception Handling.
"""


class InvalidIDException(Exception):
    # Exceptions for invalid ID input 
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class DuplicateIDException(Exception):
    # Exception for when a dupliate ID is found
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
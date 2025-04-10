# Creating custom error handling
class InvalidIDException(Exception):
    # Exceptions for invalid ID input 
    def __init__(self, message):
        # Store the message that was passed
        self.message = message
        # Behave like a real exception
        super().__init__(self.message)

class DuplicateIDException(Exception):
    # Exception for when a dupliate ID is found
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
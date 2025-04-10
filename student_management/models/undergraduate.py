from models.student import Student

class Undergraduate(Student): # Undergraduate class inherits from Student class
    def __init__(self, student_id, name, age, courses, minors=None):
        super().__init__(student_id, name, age, courses)
        # Undergrad inherits all attributes from student class
        # If minors is set, the set to the minors, else start with an empty list
        self.__minors = minors if minors else []
    
    # Return all student details + minors
    def get_details(self):
        existing_details = super().get_student_details() 
        return f"{existing_details}\nMinor: {self.__minors}"

    # Get minors 
    def get_minor(self):
        # This is as minors may not be a list
        return self.__minors if isinstance(self.__minors, list) else [self.__minors]
    
    # Update minors
    def update_minors(self, new_minors):
        # Validate new_minors is not empty/none
        if not new_minors:
            print("Error: No minors provided for update.")
            return

        # Set the new minors
        self.__minors = new_minors
        print("Minor(s) updated successfully")
        print(f"\nUpdated Minor(s):\n {', '.join(self.__minors)}")

    
    def add_minors(self, new_minors: list):
        # Convert minors into a list if not a list already
        # e.g. "Mandarin" could be a minor (minor set as a string), so when we try to append we will get an error
        if not isinstance(self.__minors, list):
            self.__minors = [self.__minors]

        # New minors is a list of new minors capitalised
        new_minors = [minor.capitalize() for minor in new_minors] 

        # Check if the new minor already exists in the existing minors
        for new_minor in new_minors:
            if new_minor in self.__minors:
                print(f"Error: minor '{new_minor}' already exists")
                # if a minor exists, move on to the next one
                continue
            # else, append the minor to the existing minors
            self.__minors.append(new_minor)
            print(f"Added: Course '{new_minor}' added for {self.get_name()}, ID: {self.get_student_id()}")

        print(f"\nUpdated Minor(s):\n {', '.join(self.__minors)}")

    def remove_minor(self, remove_minor):
        # If minors are empty, cannot remove any minors
        if len(self.__minors) == 0:
            print(f"Error: Cannot remove minors from a student with no minors")
            return
        # if the minor to be removed doesn't exist in the existing minors, cannot remove
        if remove_minor not in self.__minors:
            print(f"Error: minor '{remove_minor}' does not exist for student {self.get_name()} with ID: {self.get_student_id()}")
            return
        else:
            # Remove minor
            self.__minors.remove(remove_minor)
            print(f"Removed: minor '{remove_minor}' for {self.get_name()}, ID: {self.get_student_id()}")
    
        print(f"\nUpdated minor(s):\n {', '.join(self.__minors)}")
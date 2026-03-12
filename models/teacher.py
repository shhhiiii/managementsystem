import sqlite3  # Allows interaction with SQLite database

'''
These are custom validation functions I created (or imported from my project),
to ensure the input is clean and safe before saving anything to the database.
'''
from validation.validators import validate_integer, validate_name, validate_non_empty

'''
These are custom sorting and searching algorithms I wrote manually,
instead of relying on SQL. This shows understanding of basic algorithm design.
'''
from utilities.algorithms import bubble_sort, linear_search

# Person is a base class with shared attribute 'name'
from models.person import Person


class Teacher(Person):
    '''
    This class handles all teacher-related operations in the system.
    It inherits from the Person class to reuse the 'name' attribute logic.
    This follows OOP principles such as inheritance and encapsulation.
    '''

    def __init__(self, db):
        self.db = db  # Save reference to the database connection object

    def add_teacher(self):
        '''
        Adds a new teacher to the database after validation.
        Name is inherited from Person and assigned via self.name.
        '''
        name = validate_name("Name: ")  # Validate that name contains only letters
        subject = validate_non_empty("Subject: ")  # Ensure subject is not empty

        self.name = name  # Inherited name from Person


        try:
            # Use ? to safely insert data
            self.db.cursor.execute(
                "INSERT INTO teachers (name, subject) VALUES (?, ?)",
                (self.name, subject)
            )
            self.db.conn.commit()  # Save changes permanently
            print("Teacher added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding teacher: {e}")  # Print error if insertion fails

    def view_teachers(self):
        '''
        Displays all teachers stored in the database.
        '''
        self.db.cursor.execute("SELECT * FROM teachers") 
        rows = self.db.cursor.fetchall()

        if not rows:
            print("No teachers found.")  # If no results, inform user

        # Print each teacher in a friendly format
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Subject: {row[2]}")

    def update_teacher(self):
        '''
        Updates existing teacher details based on provided ID.
        Inputs are validated before applying changes.
        '''
        teacher_id = validate_integer("Teacher ID: ")  # Must be a valid number
        name = validate_name("New Name: ")  # Validate new name
        subject = validate_non_empty("New Subject: ")  # Validate new subject

        try:
            # Parameterized query to safely update the record
            self.db.cursor.execute(
                "UPDATE teachers SET name = ?, subject = ? WHERE id = ?",
                (name, subject, teacher_id)
            )
            if self.db.cursor.rowcount == 0:
                print("Teacher ID not found.")  # No match
            else:
                self.db.conn.commit()
                print("Teacher updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating teacher: {e}")

    def delete_teacher(self):
        '''
        Deletes a teacher from the database using their ID.
        '''
        teacher_id = validate_integer("Teacher ID: ")  # Get ID to delete

        try:
            self.db.cursor.execute("DELETE FROM teachers WHERE id = ?", (teacher_id,))
            if self.db.cursor.rowcount == 0:
                print("Teacher ID not found.")  # No match to delete
            else:
                self.db.conn.commit()
                print("Teacher deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting teacher: {e}")

    def search_teachers(self):
        '''
        Searches for a teacher by exact name using my custom linear search algorithm.
        '''
        name = validate_name("Name to search: ")  # Get name input
        self.db.cursor.execute("SELECT * FROM teachers")  
        all_teachers = self.db.cursor.fetchall()

        # Apply manual search (column 1 is the name)
        results = linear_search(all_teachers, 1, name)

        if not results:
            print("No teachers found.")  # Nothing matched
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Subject: {row[2]}")

    def sort_teachers(self):
        '''
        Sorts all teachers alphabetically by name using bubble sort.
        This shows I understand and can apply custom algorithms.
        '''
        self.db.cursor.execute("SELECT * FROM teachers")  # Get all rows
        rows = self.db.cursor.fetchall()

        sorted_rows = bubble_sort(rows, 1)  # Sort by name (index 1)

        if not sorted_rows:
            print("No teachers found.")
        for row in sorted_rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Subject: {row[2]}")
import sqlite3  # This module allows me to connect and interact with an SQLite database.

'''
These validation functions help clean and verify user input.
For example: names shouldn't contain numbers, age must be numeric and realistic, email must follow standard pattern.
'''

from validation.validators import validate_age, validate_email, validate_integer, validate_name

'''
These are basic algorithms I wrote manually to demonstrate understanding of algorithmic logic,
instead of just relying on SQL's built-in sorting or filtering.
'''

from utilities.algorithms import bubble_sort, linear_search

'''
Person is a base class that holds shared attributes like 'name'.
I use inheritance to reuse logic and follow OOP principles (R2 requirement).
'''

from models.person import Person



class Student(Person):
    '''
    This class handles all student-related operations.
    It inherits from the Person class to reuse the 'name' attribute.
    This applies OOP principles: inheritance and encapsulation.
    '''

    def __init__(self, db):
        self.db = db  # Store the database connection object passed from outside

    def add_student(self):
        '''
        Adds a new student record to the database.
        Validates name, age, and email before saving to ensure data quality.
        '''
        name = validate_name("Name: ")
        age = validate_integer("Age: ")
        email = validate_email("Email: ")

        self.name = name  # Save the name as part of the inherited attribute

        try:
            # Use parameterized SQL to avoid SQL injection and insert the new student
            self.db.cursor.execute(
                "INSERT INTO students (name, age, email) VALUES (?, ?, ?)",
                (self.name, age, email)
            )
            self.db.conn.commit()  # Commit the change to save it permanently
            print("Student added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding student: {e}")  # Show error if insertion fails

    def view_students(self):
        '''
        Displays all students from the database using SELECT query.
        '''
        self.db.cursor.execute("SELECT * FROM students")
        rows = self.db.cursor.fetchall()

        if not rows:
            print("No students found.")  # Helpful message when table is empty

        # Loop through the result set and print each student in readable format
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}")

    def update_student(self):
        '''
        Updates an existing student’s record by their ID.
        Inputs are validated and only then the UPDATE operation is attempted.
        '''
        student_id = validate_integer("Student ID: ")
        name = validate_name("New Name: ")
        age = validate_integer("New Age: ")
        email = validate_email("New Email: ")

        try:
            self.db.cursor.execute(
                "UPDATE students SET name = ?, age = ?, email = ? WHERE id = ?",
                (name, age, email, student_id)
            )
            if self.db.cursor.rowcount == 0:
                print("Student ID not found.")  # No match for ID
            else:
                self.db.conn.commit()
                print("Student updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating student: {e}")

    def delete_student(self):
        '''
        Deletes a student from the database using their ID.
        '''
        student_id = validate_integer("Student ID: ")

        try:
            self.db.cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            if self.db.cursor.rowcount == 0:
                print("Student ID not found.")  # No such student to delete
            else:
                self.db.conn.commit()
                print("Student deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting student: {e}")

    def search_students(self):
        '''
        Searches for students by name using custom linear search algorithm.
        Demonstrates understanding of search logic outside of SQL.
        '''
        name = validate_name("Name to search: ")
        self.db.cursor.execute("SELECT * FROM students")
        all_students = self.db.cursor.fetchall()

        results = linear_search(all_students, 1, name)  # Search in name column (index 1)

        if not results:
            print("No students found.")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}")

    def sort_students(self):
        '''
        Sorts students by name using bubble sort instead of SQL ORDER BY.
        Shows implementation of algorithm logic and how it's applied to data from DB.
        '''
        self.db.cursor.execute("SELECT * FROM students")
        rows = self.db.cursor.fetchall()

        sorted_rows = bubble_sort(rows, 1)  # Sort by name (index 1)

        if not sorted_rows:
            print("No students found.")
        for row in sorted_rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}")

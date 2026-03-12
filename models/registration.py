import sqlite3  # This module allows me to interact with a local SQLite database.

# I use this validation function to ensure that only valid integers are accepted as input.
from validation.validators import validate_integer


class Registration:
    '''
    This class includes course registrations, which link students to courses.
    I separated this into its own class to follow an OOP design and keep logic clean.
    It includes all CRUD (Create, Read, Update, Delete) operations for registrations.
    '''

    def __init__(self, db):
        '''
        When the class is initialized, I save the database connection and cursor
        so that I can reuse them inside every method without re-connecting each time.
        '''
        self.db = db  # databsae contains both .conn and .cursor so I can run SQL commands

    def register_student(self):
        '''
        This method registers a student to a course by asking for their IDs.

        I chose to use IDs (instead of names) because they are unique and reduce errors.
        Inputs are validated, and the record is inserted into the 'registrations' table.
        '''
        student_id = validate_integer("Student ID: ")  # Ask for valid student ID (must be a number)
        course_id = validate_integer("Course ID: ")    # Ask for valid course ID

        try:
            # I use parameterized SQL to safely insert new registration
            self.db.cursor.execute(
                "INSERT INTO registrations (student_id, course_id) VALUES (?, ?)",
                (student_id, course_id)
            )
            self.db.conn.commit()  # Save the new registration to the database
            print("Registration successful.")  # Give feedback to the user
        except sqlite3.Error as e:
            # If something goes wrong (e.g. ID not found, foreign key error), show the message
            print(f"Error registering student: {e}")

    def view_registrations(self):
        '''
        This method shows all existing registrations, including student and course names.

        I use JOINs to combine data from students and courses tables, so the user sees readable info,
        not just raw IDs. 
        '''
        self.db.cursor.execute("""
            SELECT r.id, s.name, c.name
            FROM registrations r
            JOIN students s ON r.student_id = s.id
            JOIN courses c ON r.course_id = c.id
        """)
        rows = self.db.cursor.fetchall()  # Collect all records

        if not rows:
            print("No registrations found.")  # Display if table is empty

        for row in rows:
            # Show each registration with student and course names for clarity
            print(f"ID: {row[0]}, Student: {row[1]}, Course: {row[2]}")

    def update_registration(self):
        '''
        This method updates an existing registration.

        The user can change which student is assigned to which course by updating IDs.
        Again, I validate inputs to make sure IDs are correct and positive.
        '''
        reg_id = validate_integer("Registration ID: ")        # ID of the registration to be updated
        student_id = validate_integer("New Student ID: ")     # New student ID to assign
        course_id = validate_integer("New Course ID: ")       # New course ID to assign

        try:
            # Update the registration row with new student and course IDs
            self.db.cursor.execute(
                "UPDATE registrations SET student_id = ?, course_id = ? WHERE id = ?",
                (student_id, course_id, reg_id)
            )

            if self.db.cursor.rowcount == 0:
                print("Registration ID not found.")  # No record was affected wrong ID
            else:
                self.db.conn.commit()  # Save the updated values
                print("Registration updated successfully.")
        except sqlite3.Error as e:
            # Catch and show any SQL/database-related errors
            print(f"Error updating registration: {e}")

    def delete_registration(self):
        '''
        This method deletes a registration by its ID.

        It helps clean up data when, for example, a student drops a course.
        '''
        reg_id = validate_integer("Registration ID: ")  # Ask which registration to remove

        try:
            # Delete the selected registration row
            self.db.cursor.execute("DELETE FROM registrations WHERE id = ?", (reg_id,))

            if self.db.cursor.rowcount == 0:
                print("Registration ID not found.")  # Warn if nothing was deleted
            else:
                self.db.conn.commit()  # Save the deletion
                print("Registration deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting registration: {e}")  # Show database error if something goes wrong
import sqlite3  # This module is used to work with SQLite databases

# Importing validation functions to check user input
from validation.validators import validate_integer, validate_name

# Importing custom search and sort functions that I made myself
from utilities.algorithms import bubble_sort, linear_search


class Course:
    '''
    This class includes all course-related operations.
    Such as creating, viewing, updating, deleting, searching, and sorting courses.
    '''

    def __init__(self, db):
        # Save the database connection so I can use it in all methods
        self.db = db

    def add_course(self):
        # Ask the user to enter the course name and teacher ID
        name = validate_name("Course Name: ")
        teacher_id = validate_integer("Teacher ID: ")

        try:
            # Add the new course to the database using an SQL INSERT command
            self.db.cursor.execute(
                "INSERT INTO courses (name, teacher_id) VALUES (?, ?)",
                (name, teacher_id)
            )
            # Save the change to the database
            self.db.conn.commit()
            print("Course added successfully.")
        except sqlite3.Error as e:
            # Print an error message if something goes wrong
            print(f"Error adding course: {e}")

    def view_courses(self):
        # Show all courses with their teacher names using LEFT JOIN
        self.db.cursor.execute("""
            SELECT c.id, c.name, t.name 
            FROM courses c 
            LEFT JOIN teachers t ON c.teacher_id = t.id
        """)
        rows = self.db.cursor.fetchall()

        if not rows:
            print("No courses found.")

        # Show each course. If no teacher is linked, print "None"
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Teacher: {row[2] or 'None'}")

    def update_course(self):
        # Ask the user to enter the course ID and new data
        course_id = validate_integer("Course ID: ")
        name = validate_name("New Course Name: ")
        teacher_id = validate_integer("New Teacher ID: ")

        try:
            # Update the course with new name and teacher ID
            self.db.cursor.execute(
                "UPDATE courses SET name = ?, teacher_id = ? WHERE id = ?",
                (name, teacher_id, course_id)
            )

            if self.db.cursor.rowcount == 0:
                # If no course was found with that ID, show message
                print("Course ID not found.")
            else:
                # Save the changes
                self.db.conn.commit()
                print("Course updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating course: {e}")

    def delete_course(self):
        # Ask for course ID to delete
        course_id = validate_integer("Course ID: ")

        try:
            # Delete the course from the database
            self.db.cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
            if self.db.cursor.rowcount == 0:
                print("Course ID not found.")
            else:
                self.db.conn.commit()
                print("Course deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting course: {e}")

    def search_courses(self):
        # Ask for a course name to search
        name = validate_name("Course name to search: ")
        # Get all courses from the database
        self.db.cursor.execute("SELECT * FROM courses")
        all_courses = self.db.cursor.fetchall()

        # Search using my custom linear search function
        results = linear_search(all_courses, 1, name)

        if not results:
            print("No courses found.")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Teacher ID: {row[2]}")

    def sort_courses(self):
        # Get all courses from the database
        self.db.cursor.execute("SELECT * FROM courses")
        rows = self.db.cursor.fetchall()

        # Sort the courses by name using bubble sort (my custom algorithm)
        sorted_rows = bubble_sort(rows, 1)

        if not sorted_rows:
            print("No courses found.")
        for row in sorted_rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Teacher ID: {row[2]}")

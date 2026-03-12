# Import the required classes from your project structure
from database.db import Database  # Class to connect and manage the database
from models.student import Student  # Class for managing students
from models.teacher import Teacher  # Class for managing teachers
from models.course import Course  # Class for managing courses
from models.registration import Registration  # Class for handling course registrations

class SchoolManagement:
    '''
    This is the main class that connects all parts of the system.
    It shows the main menu and submenus for Students, Teachers, Courses, and Registrationd.
    I created this as a central controller that brings all modules together.
    '''

    def __init__(self):
        '''
        I create a shared database object and pass it to all model classes.
        This way, each class works on the same database connection.
        '''
        self.db = Database()  # Create the database and tables if not already created
        self.student = Student(self.db)
        self.teacher = Teacher(self.db)
        self.course = Course(self.db)
        self.registration = Registration(self.db)

    def main_menu(self):
        '''
        This method runs the main menu loop.
        It lets the user choose which section of the system they want to manage.
        '''
        while True:
            print("\nSCHOOL MANAGEMENT SYSTEM")
            print("1. Manage Students")
            print("2. Manage Teachers")
            print("3. Manage Courses")
            print("4. Manage Registrations")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                # Student submenu includes basic CRUD and also search/sort
                while True:
                    print("\nStudent Menu")
                    print("1. Add Student")
                    print("2. View Students")
                    print("3. Update Student")
                    print("4. Delete Student")
                    print("5. Search Students by Name")  # Uses linear search
                    print("6. Sort Students by Name")    # Uses bubble sort
                    print("7. Back")

                    sub_choice = input("Enter choice: ")

                    if sub_choice == "1":
                        self.student.add_student()
                    elif sub_choice == "2":
                        self.student.view_students()
                    elif sub_choice == "3":
                        self.student.update_student()
                    elif sub_choice == "4":
                        self.student.delete_student()
                    elif sub_choice == "5":
                        self.student.search_students()
                    elif sub_choice == "6":
                        self.student.sort_students()
                    elif sub_choice == "7":
                        break
                    else:
                        print("Invalid choice.")

            elif choice == "2":
                # Teacher submenu includes search and sort using custom algorithms
                while True:
                    print("\nTeacher Menu")
                    print("1. Add Teacher")
                    print("2. View Teachers")
                    print("3. Update Teacher")
                    print("4. Delete Teacher")
                    print("5. Search Teachers by Name")  # linear_search
                    print("6. Sort Teachers by Name")    # bubble_sort
                    print("7. Back")

                    sub_choice = input("Enter choice: ")

                    if sub_choice == "1":
                        self.teacher.add_teacher()
                    elif sub_choice == "2":
                        self.teacher.view_teachers()
                    elif sub_choice == "3":
                        self.teacher.update_teacher()
                    elif sub_choice == "4":
                        self.teacher.delete_teacher()
                    elif sub_choice == "5":
                        self.teacher.search_teachers()
                    elif sub_choice == "6":
                        self.teacher.sort_teachers()
                    elif sub_choice == "7":
                        break
                    else:
                        print("Invalid choice.")

            elif choice == "3":
                # Course submenu includes search and sort by course name
                while True:
                    print("\nCourse Menu")
                    print("1. Add Course")
                    print("2. View Courses")
                    print("3. Update Course")
                    print("4. Delete Course")
                    print("5. Search Courses by Name")  # linear_search
                    print("6. Sort Courses by Name")    # bubble_sort
                    print("7. Back")

                    sub_choice = input("Enter choice: ")

                    if sub_choice == "1":
                        self.course.add_course()
                    elif sub_choice == "2":
                        self.course.view_courses()
                    elif sub_choice == "3":
                        self.course.update_course()
                    elif sub_choice == "4":
                        self.course.delete_course()
                    elif sub_choice == "5":
                        self.course.search_courses()
                    elif sub_choice == "6":
                        self.course.sort_courses()
                    elif sub_choice == "7":
                        break
                    else:
                        print("Invalid choice.")

            elif choice == "4":
                # Registration submenu handles connections between students and courses
                while True:
                    print("\nRegistration Menu")
                    print("1. Register Student to Course")
                    print("2. View Registrations")
                    print("3. Update Registration")
                    print("4. Delete Registration")
                    print("5. Back")

                    sub_choice = input("Enter choice: ")

                    if sub_choice == "1":
                        self.registration.register_student()
                    elif sub_choice == "2":
                        self.registration.view_registrations()
                    elif sub_choice == "3":
                        self.registration.update_registration()
                    elif sub_choice == "4":
                        self.registration.delete_registration()
                    elif sub_choice == "5":
                        break
                    else:
                        print("Invalid choice.")

            elif choice == "5":
                # Before exiting the system, close the DB connection
                self.db.close()
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

# This is the starting point of the program
if __name__ == "__main__":
    app = SchoolManagement()  # I create the main app instance
    app.main_menu()  # And then run the interface loop

import sqlite3  
''' 
I use SQLite because it is simple and does not need a separate server to run.
It is built into Python, so I do not need to install anything extra.
'''

class Database:
    '''
    This class is responsible for managing the database connection and setup.
    I use it to automatically create all required tables on first launch,
    which avoids setup errors.
    '''

    def __init__(self):
        '''
        When the Database class is instantiated, I connect to the SQLite file.
        If it does not exist yet, it will be created automatically.
        Then I call the function to create tables if they do not already exist.
        '''
        self.conn = sqlite3.connect("school.db")  # Connect to local databse file (or create it)
        self.cursor = self.conn.cursor()  # The cursor allows me to execute SQL statements
        self.create_tables()  # Ensure all tables are set up before anything else

    def create_tables(self):
        '''
        This function sets up all tables needed for the school system.
        I use IF NOT EXISTS to avoid errors.
        Each table has primary keys and foreign keys where appropriate.
        '''

        # STUDENTS TABLE
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER CHECK(age >= 4 AND age <= 20),
                email TEXT UNIQUE NOT NULL
            );
        """)  # student id, name, age with constraint, unique email

        # TEACHERS TABLE
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                subject TEXT NOT NULL
            );
        """)  # teacher id, name and subject

        # COURSES TABLE
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                teacher_id INTEGER,
                FOREIGN KEY(teacher_id) REFERENCES teachers(id)
            );
        """)  # courses link to teacher via teacher_id

        # REGISTRATIONS TABLE
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS registrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                course_id INTEGER,
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(course_id) REFERENCES courses(id)
            );
        """)  # links students and courses together

        self.conn.commit()  # Save changes

    def close(self):
        '''
        This method closes the connection to the database.
        I call it at the end of the program to release system resources.
        '''
        self.conn.close()

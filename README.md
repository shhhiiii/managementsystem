School Management System
Project Overview
This is a lightweight, command-line-based School Management System. The system provides a user-friendly interface to manage core school entities, including students, teachers, courses, and their registrations. It is built using Python for the core logic and SQLite for persistent data storage.
+3

Key Features
Full CRUD Operations: Create, Read, Update, and Delete records for Students, Teachers, Courses, and Registrations.
+1
Search and Sort: Includes built-in algorithms to sort records alphabetically (using Bubble Sort) and search for specific entities by name (using Linear Search).
+1
Robust Data Validation: Ensures data integrity by validating inputs, such as enforcing age constraints (4 to 20 years), checking for empty fields, and verifying email formats using regular expressions.
+3
Interactive CLI: Easy-to-use menu-driven interface built with Python loops and conditional statements.
+1
Relational Data Management: Links students to courses and courses to teachers while maintaining referential integrity.

Technologies Used
Language: Python 3 
+1
Database: SQLite3 (Serverless, file-based relational database) 
+1
Design Paradigm: Object-Oriented Programming (OOP) 

System Architecture & OOP Principles
The codebase is heavily modularized, following strict Object-Oriented Programming principles:
Inheritance: A central Person base class handles shared attributes (like name), which is inherited by both Student and Teacher classes to avoid code duplication.
Encapsulation: Logic and CRUD operations are grouped within their respective dedicated classes (Student, Teacher, Course, Registration).
Controller Pattern: A main SchoolManagement class acts as the central controller connecting all system modules and managing the database state.

Database Schema
The database uses a normalized relational structure (up to 3rd Normal Form) to eliminate redundancy:
students: id (PK), name, age (CHECK constraints applied), email (UNIQUE) 
teachers: id (PK), name, subject 
courses: id (PK), name, teacher_id (FK referencing teachers) 
registrations: id (PK), student_id (FK referencing students), course_id (FK referencing courses) 

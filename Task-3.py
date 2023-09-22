'''
Task 3: MySQL Database Operations with Python ( Compulsory )

Problem Statement:
Your task is to write a Python program that accomplishes the following:
First create a database , table and add these column ‘student_id’, ‘first_name’, ‘last_name’,
‘age’, ‘grade’.
Connects to your MySQL database with python.
Inserts a new student record into the "students" table with the following details:
First Name: "Alice"
Last Name: "Smith"
Age: 18
Grade: 95.5
Updates the grade of the student with the first name "Alice" to 97.0.
Deletes the student with the last name "Smith."
Fetches and displays all student records from the "students" table.
'''

import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host="localhost",           # typically "localhost"
    user="root",       # e.g. "root"
    password="132513"
)

cursor = connection.cursor()

# Create a database
cursor.execute("CREATE DATABASE IF NOT EXISTS studentDB")

# Connect to the created database
cursor.execute("USE studentDB")

# Create a table named "students"
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    grade DECIMAL(5, 2)
)
""")

# Insert student record into "students" table
cursor.execute("INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)", ("Alice", "Smith", 18, 95.5))
connection.commit()

# Update grade of student "Alice"
cursor.execute("UPDATE students SET grade = %s WHERE first_name = %s", (97.0, "Alice"))
connection.commit()

# Delete student with last name "Smith"
cursor.execute("DELETE FROM students WHERE last_name = %s", ("Smith",))
connection.commit()

# Fetch and display all student records
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

for student in students:
    print(student)

cursor.close()
connection.close()
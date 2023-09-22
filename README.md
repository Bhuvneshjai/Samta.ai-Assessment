# Samta.ai Assessment

## Task 1: Calculate Area with Conditions
1.  Objective:
    * Write a function to calculate the area of a rectangle.
    * Add a condition to check if the rectangle is a square.
2. Function Name: function_area
3. Parameters:
    * length: Length of the rectangle.
    * width: Width of the rectangle.
4. Functionality:
    * If length is equal to width, the function returns "This is a square!".
    * Otherwise, it calculates the area by multiplying length and width and returns the result.
5. User Interaction:
    * Prompt the user to input values for length and width.
    * Call the function_area with user input values.
    * Display either the area of the rectangle or the message indicating it's a square.

## Task 2: Generate Fibonacci Series
1. Objective:
    * Write a program that generates the Fibonacci sequence up to a specified number of terms.
2. Function Name: fibonacci_sequence
3. Parameter:
    * n: Number of terms required in the Fibonacci sequence.
4. Functionality:
    * The function initializes the sequence with the first two numbers 0 and 1.
    * It calculates subsequent numbers as the sum of the two preceding ones.
    * Continues this process up to n terms.
5. User Interaction:
    * Prompt the user to input the number of terms (n) they want in the sequence.
    * Call the fibonacci_sequence function with the user's input value.
    * Display the Fibonacci sequence up to the specified number of terms.

## Task 3: MySQL Database Operations with Python ( Compulsory )
1. Database Connection:
    * Using the mysql.connector library, a connection to the MySQL server is established.
    * It connects with the hostname localhost, the user root, and the specified password.

2. Database Creation:
    * If a database named studentDB does not already exist, it gets created.

3. Setting Active Database:
    * The script then uses the studentDB for further operations.

4. Table Creation:
    * Inside the studentDB database, a table named students is created if it doesn't already exist.
    * This table has the following columns: student_id (auto-incremented primary key), first_name, last_name, age, and grade.

5. Inserting a Record:
    * A student record with details "Alice Smith", age 18, and grade 95.5 is inserted into the students table.

6. Updating a Record:
    * The grade of the student with the first name "Alice" is updated to 97.0.

7. Deleting a Record:
    * The student with the last name "Smith" is deleted from the students table.

8. Fetching and Displaying Records:
    * The script fetches all records from the students table.
    * Each student record is then printed to the console.

9. Closing the Connection:
    * The cursor and the connection to the MySQL server are closed, ending the database operations.
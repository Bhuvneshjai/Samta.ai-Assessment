'''
Task 2: Generate Fibonacci Series

Problem Statement:
Write a Python program that generates the Fibonacci sequence up to a specified number of
terms, n. The Fibonacci sequence starts with 0 and 1, and each subsequent number in the
sequence is the sum of the two preceding numbers (e.g., 0, 1, 1, 2, 3, 5, 8, ...). Prompt the
user to enter the number of terms (n) they want in the sequence and then display the
Fibonacci sequence up to that number of terms.
'''

def fibonacci_sequence(n):
    if n <= 0:
        return []
    a, b = 0, 1
    lst = [a]
    if n > 1:
        lst.append(b)
    for i in range(2,n):
        a,b = b, a+b
        lst.append(b)
    return lst

n = int(input("Enter Number : "))
result = fibonacci_sequence(n)
for i in result:
    print(i, end=' ')
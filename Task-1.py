''' 
Task 1: Calculate Area with Conditions
Write a Python function calculate_area that takes two parameters: length and width. It
should calculate and return the area of a rectangle. However, add a condition: if the length
is equal to the width, return "This is a square!" instead of the area. Then, write a program to
input values for length and width from the user and call the calculate_area function to
display either the area or the message. 
'''

def function_area(length, width):
    if length == width:
        return "This is a square!"
    return length * width

l = int(input("Enter Length : "))
w = int(input("Enter Width : "))

result = function_area(l,w)
print(f"Result : {result}")
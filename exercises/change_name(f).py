"""Assign a different name to function and call it through the new name"""

def displayStudent(name, age):
    print(name, age)

showStudent = displayStudent
showStudent("Emma", 26)
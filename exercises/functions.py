"""Write a function calculation() such that it can accept two variables and calculate the 
addition and subtraction of it. And also it must return both addition and subtraction in a single return call
#may be try this with function in class"""

def calculation(a, b):
    return a+b
print(calculation(40,10))


"""Create a function showEmployee() in such a way that it should 
accept employee name, and it’s salary and display both, and if the salary is missing in
 function call it should show it as 9000"""

 #default functions

def showEmployee(name, salary=9000):
    salary=9000

    return f"Ben earns {salary}"

print(showEmployee('Ben'))


"""Assign a different name to function and call it through the new name"""

def displayStudent(name, age):
    print(name, age)

showStudent = displayStudent
showStudent("Emma", 26)
















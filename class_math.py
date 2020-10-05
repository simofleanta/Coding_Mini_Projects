
""" Lucia gave awy a box of 44 sweets. She gave her two brothers,each, 13 sweets. How many sweets are left for Lucia?
Solve the basic maths problem using class"""

#create class with a,b attributes
#define math with self, a,b arguments that prints maths formula
#create Math object.

class maths:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def math(self,a,b):
        print(a-b*2)

   
Math=maths(44,13)
print(Math.a)
print(Math.b)
print(Math.math(44,13))

#------------------------------------------------------------

#var 2
#using a for loop to add a,b 

def math(a,b):
    arguments=a,b
    total=0
    for x in arguments:
        total = a-b*2
    return total   
print(math(44,13))
#-----------------------------------------
"""change function name"""

def displayStudent(name, age):
    print(name, age)

studentName=displayStudent

print(studentName("Emma", 26))












 
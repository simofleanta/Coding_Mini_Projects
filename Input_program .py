
"""Arithmetic problem solution using taking decision input
problem 1. How many tulips are there left
problem 2. How many sweets are there left. 
If user chooses not to calculate the program transfers you to sweets problem
If user chooses to calculate the program returns the tulips problem solution
if user chooses Soso the program exists
"""

#branch_function of the problems
#functions with input that asks 
#function that performs the yes no question
#builtin function exit if user wants to exit


def math(c,d):
    if c>d:
        print(c-d*2)
    else:
        print(None)

def ar(a,b):
    if a>b:
        print(a-b)
    else:
        print(None)

def decide():
    print("Continue challenge")
    input()
    print("sure? ")
    answer()

def answer():
    """generates input yes or no """
    print ('solve the problem? :[No/Yes/Soso] ')
    reply = input()
    if reply == 'No':
        math(44,13)                
    elif reply == 'Yes':
        ar(36,28)
    elif reply == 'Soso':
        exit()

decide()








#df the function

def add(x,y):
    """this f adds"""
    return x+y
def subtract(x,y):
    """this f subtracts"""
    return x-y
def multiply(x,y):
    """this f multiply"""
    return x*y
def divide(x,y):
    """this f divides"""
    return x/y


#take imput from user
while True:

    print("Please select the opp.")
    print("1.Add")
    print("2.Substract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")    
    choice = input("Enter choice(1/2/3/4/5):")

if choice=='1':
    num1=int(input("Enter first number: "))
    num2=int(input("Enter the second number: "))
    print(num1, "+", num2,"=", add(num1,num2))
elif choice=='2':
    num1=int(input("Enter first number: "))
    num2=int(input("Enter the second number: "))
    print(num1, "-", num2,"=", subtract(num1,num2))

elif choice=='3':
    num1=int(input("Enter first number: "))
    num2=int(input("Enter the second number: "))
    print(num1, "*", num2,"=", multiply(num1,num2))

elif choice=='4':
    num1=int(input("Enter first number: "))
    num2=int(input("Enter the second number: "))
    print(num1, "/", num2,"=", divide(num1,num2))

else:
    choice=='5'














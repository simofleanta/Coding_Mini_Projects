#####################################
# ScriuCod - Python - OOP - Exercises
#####################################

# Please read carefully each exercise definition
# Do not rename the class or functions names or verification will not work
# Use docstrings on classes and methods

# Complete the tasks below by writing classes with attributes and methods! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical steps.


#####################
# Exercise 1
#####################

# Create a circle class and initialize it with radius.
# Make two methods get_area and get_circumference inside this class.

class Circle:
    def __init__(self, radius):
        self.radius=radius

    def get_area(self):
        pass  # YOUR CODE GOES HERE, REMOVE PASS

    def get_circumference(self):
        pass  # check function in class


#####################
# Exercise 2
#####################

# Create a temperature class. Make two methods :
# 1. convert_fahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convert_celsius - It will take Fahrenheit and will convert it into Celsius.

class Temperature:
    def convert_fahrenheit(self, celsius):
        pass  # YOUR CODE GOES HERE, REMOVE PASS

    def convert_celsius(self, fahrenheit):
        pass  # YOUR CODE GOES HERE, REMOVE PASS


#####################
# Exercise 3
#####################

# Create a Student class and initialize it with name and roll number.
# Make methods to :
# 1. display - It should display all information of the student.
# 2. set_age - It should assign age to student(setter and get?)
# 3. set_marks - It should assign marks to the student.

class Student:
    def __init__(self, name, roll):
        self.name=name
        self.roll=roll
    
    def display(self):
        print(f"{self.name} and {self.roll}")

        
    def set_age(self,age):
        self._age=age

    def set_marks(self,marks):
        self._marks=marks

p=Student('Adrian',2)
p.set_age(36)
p.set_marks([10,1,5])

#get age
print(p.get_age())   
print(p._age) 
#get marks
print(p.get_marks())
print(p._marks)
    





#####################
# Exercise 4
#####################

# Create a Time class and initialize it with hours and minutes.
# 1. Make a method add_time which should take two time object and add them.
# Example: (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# 2. Make a method display_time which should print the time.
# 3. Make a method display_minute which should display the total minutes in the Time.
# Example: (1 hr 2 min) should display 62 minute.

class Time:

    def __init__(self, hours, minutes):
        pass  # YOUR CODE GOES HERE, REMOVE PASS

    def add_time(self, t1, t2):
        pass  # YOUR CODE GOES HERE, REMOVE PASS

    def display_time(self):
        pass  # YOUR CODE GOES HERE, REMOVE PASS

    def display_minute(self):
        pass  # YOUR CODE GOES HERE, REMOVE PASS


#####################
# Exercise 5
#####################

# Define property that should have the same value for every class instance

# Expected Output:
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

# Bonus:
# Create a new Motorbike class that will have color blue

# Use the following code for this exercise.
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass  # YOUR CODE GOES HERE, REMOVE PASS


class Car(Vehicle):
    pass  # YOUR CODE GOES HERE, REMOVE PASS


#####################
# Exercise 6
#####################

# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a
# default value of 50.

# Expected Output:
# The seating capacity of a bus is 50 passengers

# Use the following code for your parent Vehicle class.
# You need to use method overriding.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self):
        pass  # YOUR CODE GOES HERE, REMOVE PASS


#####################
# Exercise 7
#####################

# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating
# capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

# Note: The bus seating capacity is 50. so the final fare amount should be 5550. You need to override the fare()
# method of a Vehicle class in Bus class.

# Expected Output:
# Total Bus fare is: 5500.0

# Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a
# child class.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    pass  # YOUR CODE GOES HERE, REMOVE PASS


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


#####################
# Exercise 8
#####################

# Determine if School_bus is also an instance of the Vehicle class

# Expected Output:
# True


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass  # YOUR CODE GOES HERE, REMOVE PASS


#####################
# Exercise 8
#####################

# Create a classes structure for the products E-mag https://www.emag.ro/
# Limit the tree at maximum 3 children per parent
# Products
#     Computers
#         Laptops
#         Desktops
#         Components
#             CPU
#             GPU
#             Motherboards
#     TV
#         HD
#         OLED
#         4K
#     Fashion

# Use attributes and methods to build items characteristics (tech specifications) and features (what they can do)

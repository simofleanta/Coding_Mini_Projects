#####################################
# ScriuCod - Python - OOP - Exercises
#####################################

# Please read carefully each exercise definition
# Do not rename the class or functions names or verification will not work
# Use docstrings on classes and methods

# Complete the tasks below by writing classes with attributes and methods! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical steps.








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

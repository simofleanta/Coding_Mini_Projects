
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
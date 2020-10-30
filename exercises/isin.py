# Determine if School_bus is also an instance of the Vehicle class

# Expected Output:
# True


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass

School_bus=("School Volvo", 22,50)
print(isinstance(School_bus, Vehicle))
print(type(School_bus))

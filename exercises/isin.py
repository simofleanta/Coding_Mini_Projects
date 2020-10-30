
# The default fare charge of any vehicle is seating
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
    def __init__(self, name,max_speed, mileage):
        super().__init__(name,max_speed,mileage)
    
    def full_amount(self):
        return self.capacity * 100+10/100


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
print("Full amount: ", School_bus.full_amount())



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

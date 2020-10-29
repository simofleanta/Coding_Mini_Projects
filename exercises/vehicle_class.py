
# Define property that should have the same value for every class instance

# Expected Output:
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

# Bonus:
# Create a new Motorbike class that will have color blue

# Use the following code for this exercise.
class Vehicle:

    color="White"
   
    def __init__(self, name,max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print_v(self):
        print(self.color,self.name,self.max_speed,self.mileage)

v=Vehicle('School Volvo', 180, 12) 

print("Vehicle name:", v.name, v.color, v.max_speed,v.mileage)    


class Bus(Vehicle):
    def __init__(self, name,max_speed, mileage):
        super().__init__(name,max_speed,mileage)
        self.name='Audi Q5'
        self.speed=240
        self.mileage=18
        
    def print_bus(self):
        print(self.name, self.color,self.speed,self.mileage)

B=Bus('Audi Q5', 240,18)

print("Bus name: ", B.name, B.color, B.speed, B.mileage)

class Car(Vehicle):
    pass  # YOUR CODE GOES HERE, REMOVE PASS
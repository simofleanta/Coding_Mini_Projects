
# Define property that should have the same value for every class instance
# Expected Output:
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18
# Bonus:
# Create a new Motorbike class that will have color blue


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
        self.seat_capacity=50
        
    def print_bus(self):
        print(self.name, self.color,self.speed,self.mileage)

B=Bus('Audi Q5', 240,18)

print("Bus name: ", B.name, B.color, B.speed, B.mileage, B.seat_capacity)

class Car(Vehicle):
    def __init__(self, name,max_speed, mileage):
        super().__init__(name,max_speed,mileage)
        self.capacity=5
c=Car('Dacia', 180, 17)
print("Car :", c.name, c.color,c.max_speed,c.mileage)

class Motorbike(Vehicle):
    def __init__(self, name,max_speed, mileage):
        super().__init__(name,max_speed,mileage)
        self.color="Blue"
        self.capacity=600

m=Motorbike('Honda', 260, 80)
print("Motorbike :", m.name, m.color,m.max_speed,m.capacity,m.mileage)


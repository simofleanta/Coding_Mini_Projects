

# Create a circle class and initialize it with radius.
# Make two methods get_area and get_circumference inside this class.

class Circle:
    def __init__(self, radius,area=0,circumference=0):
        self.radius=radius
        self._area=area
        self.circumference=circumference

    def get_area(self):
        return self.get_area 

    def get_circumference(self):
        return self.get_area 
    
    def set_area(self,a):
        self._area=a
    
    def set_circumference(self,a):
        self._circumference=a

p = Circle(0.2) 

# retrieving age using getter 
print(p.get_area()) 
print(p._area)
print(p.get_circumference())
print(p.circumference)
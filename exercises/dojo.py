

# Create a circle class and initialize it with radius.
# Make two methods get_area and get_circumference inside this class.

class Circle:
    def __init__(self, radius,area=0,circumference=0):
        self.radius=radius
        self._circumference=circumference
        self._area=area
    
    def get_area(self):
        return self._area
    def set_area(self,a):
        self._area=a
    def get_circumference(self):
        return self._circumference
    def set_circumference(self,a):
        self._circumference=a
p=Circle(20)


 


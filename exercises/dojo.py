
#display all attributes
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




 


    

      
      
      
      
      
      
      
      
      
      
      
      
"""return "{} age {}".format(self.name, self.roll)


    def set_marks(self, marks):
        return "{} marks {}".format(self.name, self.roll,self.marks)

    def display(self):
        print(f"{self.name} and {self.roll}, and {self.age} and {self.marks}")

p=Student('Adrian',2,36,10)
p.display()"""


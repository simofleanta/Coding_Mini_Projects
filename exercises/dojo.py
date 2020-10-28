
#display all attributes
class Student:
    def __init__(self, name, roll):
        self.name=name
        self.roll=roll


    def display(self):
        print(self.name,self.roll)
        print(f"i am {self.name} and {self.roll}")#using formater
        
        

    def set_age(self, age):
      return "{} age {}".format(self.name, self.roll)
    
    def set_marks(self, marks):
        return "{} marks {}".format(self.name, self.roll,self.marks)

    
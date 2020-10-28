
#display all attributes
class Student:
    def __init__(self, name, roll):
        self.name=name
        self.roll=roll

        
    def set_age(self, age):
      return "{} age {}".format(self.name, self.roll)


    def set_marks(self, marks):
        return "{} marks {}".format(self.name, self.roll,self.marks)

    def display(self):
        print(f"{self.name} and {self.roll}, and {self.age} and {self.marks}")

    
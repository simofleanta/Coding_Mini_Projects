class Student: 
    def __init__(self, name,roll,age = 0, marks=0): 
         self._age = age 
         self.name=name
         self.roll=roll
         self._marks=marks
         
      
    # getter method 
    def get_age(self): 
        return self._age 
      
    # setter method 
    def set_age(self, x): 
        self._age = x 
    
    # getter method 
    def get_marks(self): 
        return self._marks
    
    def set_marks(self, x): 
        self._marks = x 
    
  
p = Student('Adrian',2) 
  
# setting the age using setter 
p.set_age(36) 
p.set_marks([1,2,3])
  
# retrieving age using getter 
print(p.get_age()) 
print(p._age)
print(p.get_marks())
print(p._marks)




  







#p=Student('Adrian',2)
#p.set_age(36)
#p.set_marks([10,1,5])




 


    

      
      
      
      
      
      
      
      
      
      
      


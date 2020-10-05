""" find x values for the following situ:"""
#creating inherited class to chain 2 exercises expressions 

class x:
    def __init__(self,x):
        self.x=x
    
    def f(self,x):
        return 17-x>=11

p=x(-5)

print(p.f(-5))

class y(x):
    def __init__(self,x):
        self.x=x
    
    def f(self,x):
        return 24-x>20

a=x(10)
print(a.f(1))
print(a.f(11))

class z(y):
    def __init__(self,x):
        self.x=x
    
    def f(self,x):
        return x+28<=31
    
    b=y(100)
    print(b.f(100))
    print(b.f(-3))












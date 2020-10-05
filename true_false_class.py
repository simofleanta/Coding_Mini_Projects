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


"""which of these expressions are true?
12-3<3
9-7!=3
"""

class bul:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def statement(self,a,b):
        if a-b!=3:
            return False 
        else:
            return bool

s=bul(9,7)
print(s.statement(9,7))

class ex(bul):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def c(self,a,b):
        if a-b<10:
            return False 
        else:
            return bool

d=ex(12,3)
print(d.c(12,3))



    




    

















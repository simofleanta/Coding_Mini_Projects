""" There is a unkown positive integer n. We know:
n % 3 = 2, and n % 5 = 3, and n % 7 = 2.
What's the minimum possible positive integer n? """

#making class of the math function


class x:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def ex(self,x,y,z):
        for i in range(0,1000):
            if i%3==x and i%5==y and i%7==z:
                return(i)


findx=x(1,2,3)
print(findx.x)
print(findx.y)
print(findx.z)
print(findx.ex(1,2,3))





        



"








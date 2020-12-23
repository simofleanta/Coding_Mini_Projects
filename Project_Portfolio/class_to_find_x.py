""" There is a unkown positive integer n. We know:
n % 3 = 2, and n % 5 = 3, and n % 7 = 2.
What's the minimum possible positive integer n? """

#making class to find x


class find_x:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def ex(self,x,y,z):
        for n in range(0,1000):
            if n%3==x and n%5==y and n%7==z:
                return(n)


findx=find_x(6,8,9)
print(findx.x)
print(findx.y)
print(findx.z)
print(findx.ex(6,8,9))







        







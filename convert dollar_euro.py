
# creating a program that converts currency unsing manual conversion formula 
# I used class methods to do it. 
#I took the rated from google. 


class currency:
 
    def __init__(self, euro, dollar):
        self.euro=euro
        self.dollar=dollar
        
    def to_euro(self, dollar):
        return dollar * 1.21      

    def to_dollar(self, euro):
        return euro * 0.82


convert=currency('euro','dollar')


print(convert.euro)
print(convert.dollar)
print("conversions :", convert.to_euro(500),convert.to_dollar(200))






















   
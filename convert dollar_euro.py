
# Create a temperature class. Make two methods :
# 1. convert_fahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convert_celsius - It will take Fahrenheit and will convert it into Celsius.
#currency convert 

#version 1
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
print("conversions :", convert.to_euro(2),convert.to_dollar(4))






















   
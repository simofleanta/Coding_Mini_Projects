
# Create a temperature class. Make two methods :
# 1. convert_fahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convert_celsius - It will take Fahrenheit and will convert it into Celsius.

class Temperature:
    def __init__(self, fahrenheit,celsius):
        self.fahrenheit=fahrenheit
        self.celsius=celsius

    def t(self):
        print(self.fahrenheit,self.celsius)


    def convert_fahrenheit(self, celsius=20):
        return (celsius * 9/5) + 32

         

    def convert_celsius(self, fahrenheit=50):
        return (fahrenheit - 32) * 5/9


    
      
 

p=Temperature(50,20)
p.t()
print("conversions :", p.convert_celsius,p.convert_fahrenheit)
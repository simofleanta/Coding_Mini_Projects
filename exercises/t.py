
# Create a temperature class. Make two methods :
# 1. convert_fahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convert_celsius - It will take Fahrenheit and will convert it into Celsius.


class Temperature:
 
    def __init__(self, celsius, fahrenheit):
        self.celsius=celsius
        self.fahrenheit=fahrenheit
        
    def convert_fahrenheit(self, celsius=20):
        return((self.celsius * 9/5) + 32)

         

    def convert_celsius(self, fahrenheit=50):
        return((self.fahrenheit - 32) * 5/9)

 

p=Temperature('celsius','fahrenheit')
print("conversions :", p.convert_celsius,p.convert_fahrenheit)















"""class Temperature:
    t=0
    def __init__(self, temperature):
        self.temperature=temperature     
    


    def convert_fahrenheit(self):
        t=float((self.temperature * 9)/5 + 32)
        return t

         

    def convert_celsius(self):
        t=float((self.temperature - 32) * 5/9)
        return t

 

p=Temperature(50)
print("conversions :", p.convert_celsius,p.convert_fahrenheit)"""
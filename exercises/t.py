
# Create a temperature class. Make two methods :
# 1. convert_fahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convert_celsius - It will take Fahrenheit and will convert it into Celsius.


class Temperature:
 
    def __init__(self, celsius, fahrenheit):
        self.celsius=celsius
        self.fahrenheit=fahrenheit
        
    def convert_fahrenheit(self, celsius=20):
        return((celsius * 9/5) + 32)

         

    def convert_celsius(self, fahrenheit=50):
        return((fahrenheit - 32) * 5/9)

 
t=Temperature('celsius','fahrenheit')
print("conversions :", t.convert_celsius,t.convert_fahrenheit)

t=input("into celsius: ")
print(t)
t1=input("into F: ")
print(t1)












   
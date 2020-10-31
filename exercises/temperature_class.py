
# Create a temperature class. Make two methods :
# 1. convert_fahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convert_celsius - It will take Fahrenheit and will convert it into Celsius.

#version 1
class Temperature:
 
    def __init__(self, celsius, fahrenheit):
        self.celsius=celsius
        self.fahrenheit=fahrenheit
        
    def convert_fahrenheit(self, celsius):
        return((celsius * 9/5) + 32)         

    def convert_celsius(self, fahrenheit):
        return((fahrenheit - 32) * 5/9)


def decide():
    print("convert?")
    input()
    print("sure")
    answer()

 
def answer():
    print('into: [C/F]')
    reply=input()
    if reply=='C':
        print(Temperature.convert_fahrenheit(3))
    elif reply=='F':
        print(Temperature.convert_celsius(2))
    else:
        return None

decide()



t=Temperature('fahrenheit','celsius')



#print(t.fahrenheit)
#print(t.celsius)
#print("conversions :", t.convert_celsius(2),t.convert_fahrenheit(4))

#version2 

class t:
    def __init__(self, c,f):
        self.c=c
        self.f=f

    
    def convert_temp(self,c,f):
        return ((c - 32) * 5/9),((f - 32) * 5/9)

#C=t('fahrenheit','celsius')
#print("conversions :", C.convert_temp(2,3))




















   
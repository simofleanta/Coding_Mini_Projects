

def convert_fahrenheit(celsius):
        return((celsius * 9/5) + 32)         

def convert_celsius(fahrenheit):
        return((fahrenheit - 32) * 5/9)


def decide():
    print("convert?")
    input()
    print("sure")
    answer()

 
def answer():
    print('into: [celsius/fahrenheit]')
    reply=input()
    if reply=='celsius':
        print(convert_celsius(5))
    elif reply=='fahrenheit':
        print(convert_fahrenheit(2))
    else:
        exit()

decide()
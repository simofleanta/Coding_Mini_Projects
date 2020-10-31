





def decide():
    print("convert?")
    input()
    print("sure")
    answer()

 
def answer():
    print('into: [C/F]')
    reply=input()
    if reply=='celsius':
        print(convert_celsius(5))
    elif reply=='fahrenheit':
        print(convert_fahrenheit(=2))
    else:
        exit()

decide()
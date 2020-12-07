import random

"""Guess my age """

#generate a random number of two digits
#ask
#generate hints using if 
#to keep playing the user guess you need to enumerate num in range code
#perform while loop 



def ask():
    """ asks question"""
    return list(input("How old are you?"))

def generate_random_age():
    """ generate random number"""
    digits=[str(num) for num in range(10)]
    random.shuffle(digits)
    print(digits[:2])
    return digits[:2]

def generate_age_hints(code,user):
    """ Generating hints"""

    if user==code:
        return "Cracked"

    hints=[]
    

    for ind,num in enumerate(user): 
        if num == code[ind]:
            hints.append("that is right")
        elif  num in code:
            hints.append("Almost there")
    
    if hints == []:
        return ["No way"]
    else:
        return hints

print("mno")


secret_age=generate_random_age()

ageReport=[]
    

while ageReport != "Cracked":
    guess=ask()

    ageReport=generate_age_hints(guess, secret_age)

    for hint in ageReport:
        print(hint)

def conditions(guess,secret_age):
    for i in enumerate(secret_age):
        if len(guess) > secret_age:
            print("Too big")


"""Contunue the game"""

#figuered out the easiest way to generate a yes no answer code
#a function that questions 
#a function that inputs yes and no with if 


def decide():
    print("Now that the age was guessed, I want you to guess my name")
    input()
    print("ok? ")
    answer()

def answer():
    """generates input yes or no """
    print ('Answer :[Yes/No] ')
    reply = input()
    if reply == 'Yes':
        answer()
    elif reply == 'No':
        exit()

decide()













   












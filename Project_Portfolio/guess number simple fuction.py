""" I know I've been jingeling o this little game but I am trying to find my own way of creating the 
program"""
import random

def guess_it(x):
    """ function creating a random number"""
    random_x=random.randint(1,x)
    guess=0 # so tht guess will never ==0, hence
    while guess_it != random_x: #while the function not coincide the random_x var, the loop will keep playing. It will break when function guess_it ==random(x)
        #added guess in integer input so that the answer is an int. 
        guess=int(input(f'guess a number between 1 and {x}: '))
        #guess would help creating the if clauses. 
        if guess < random_x:
            print('too low high, try again')
        elif guess > random_x:
            print('too high , try again')
        else:
            print('Yup you got it {random_x}')

#call function
print(guess_it(20))
       

        






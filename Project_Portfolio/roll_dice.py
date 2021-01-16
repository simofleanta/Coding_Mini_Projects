import random

min=1
max=6

roll="go"

while roll=="go" or roll=="yes":
    print("Rolling")
    print("The number is...")
    print(random.randint(min,max))
    print(random.randint(min,max))

    roll=input("roll_it_again")


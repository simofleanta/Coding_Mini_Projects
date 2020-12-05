import random

#pass symbols
low="abcd"
Caps="ABCD"
No="012345"
Sy=".;*/,[],]"

#gather all chars into a var
all_c=low+Caps+No+Sy
#set length
length=16
#function
#password generator function
def pass_gen(all_c,length):
    """Creating a password with function that randomly joins chars"""
    return "".join(random.sample(all_c,length))
print(pass_gen(all_c,length))












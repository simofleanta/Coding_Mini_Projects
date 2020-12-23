import random

#pass symbols
low="abcdefghij"
Caps="ABCD"
No="012345678"
Symbols=".;*/,[],]{'"

#gather all symbols
gather_symbols=low+Caps+No+Symbols

#set length
length=8

#function to generate pass
def generate_password(gather_symbols, length):
    """function to generate pass"""
    return "".join(random.sample(gather_symbols,length))
print(generate_password(gather_symbols,length))









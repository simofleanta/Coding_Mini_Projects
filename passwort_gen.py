import random

#pass symbols

low="abcd"
Caps="ABCD"
No="012345"
Sy=".;*/,[],{}]"

all_c=low+Caps+No+Sy
length=16
password="".join(random.sample(all_c,length))
print(password)
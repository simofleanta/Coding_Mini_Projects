import random

#pass symbols

low="abcd"
Caps="ABCD"
No="012345"
Sy=".;*/,[],]"

#gather all chars
all_c=low+Caps+No+Sy
#set length
length=16
#join all chars randomly using random.sample
password="".join(random.sample(all_c,length))
print(password)


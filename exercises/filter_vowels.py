
l=['a','b','c','d','e','f','g','r','h','i','j','k','m','n','o','u','z','x','s']
def vowelletters_filter(l):
    vowels=['a','e','i','o','u']
    if (l in vowels):
        return True
    else:
        return False
#calling f        
vowelletters_filter=filter(vowelletters_filter,l)
for vowel in vowelletters_filter:
    print (vowel)

    

"""Given the string print various letters using slicing:"""
name = 'django'
# Use indexing to print out the following:
# 'd'
#reverse django

print(name[:-1])
print(name[::-1])

#reverse using function that returns reversed object
def rev(string):
    string='django'
    return reversed(string)

print(rev('django'))

print(name[0])
print(name[0:4])
print(name[0:2:4])


def name(case1):
    """ function to return middle three chars from a str for scenatio 1"""
    char_midle=int(len(case1)/2)
    return case1[3:6]
    
print(name('django'))

def name(case2):
    """ function to return middle three chars from a str for scenatio 1"""
    char_midle=int(len(case2)/3)
    return case2[char_midle-1:char_midle+2]   
print(name('django'))

#-----------------------------------------------------------------------------------------


""" Given a string of odd length greater 7, return a string made of the middle three chars of a given String"""
str1 = "JhonDipPeta" #Dip
str2 = "JaSonAy"     #Son


#use functions 
def char(scenario1):
    """ function to return middle three chars from a str for scenatio 1"""
    char_midle=int(len(scenario1)/2)
    return scenario1[char_midle-1:char_midle+2]
print(char('JhonDipPeta'))


def chars(scenario2):
    """ function to return middle three chars from a str for scenatio 1"""
    chars_midle=int(len(scenario2)/2)
    return scenario2[chars_midle-1:chars_midle+2]
print(char('JaSonAy'))








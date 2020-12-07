"""# Given this nested list:
nested_lst= [3, 7, [1, 4, 'hello']]
# Reassign "hello" to be "goodbye"""

nested_lst= [3, 7, [1, 4, 'hello']]
nested_lst[2][2]=['goodbye']
print(nested_lst)

#--------------------------------------------------

# Join all list's elements with: " + "

lst = ["Paris", "London", "Madrid", "Bucharest", "Brasov"]

def join(lst):
    """returns joind list with +"""
    lst = ["Paris", "London", "Madrid", "Bucharest", "Brasov"]

    return '+'.join(lst)

print(join(lst))

# create a list from a string
#var1
text = 'comprehension'
n=list(text)
print(n)

#var2
n=text.split()
print(n)
print(type(n))



#Given a Python list you should be able to display Python list in the following order

aLsit = ([100, 200, 300, 400, 500])

def slice(list):
    return list[::-1]
print(slice([100, 200, 300, 400, 500]))















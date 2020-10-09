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

# From below list create a new list with unique elements:
numbers = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
n=set(numbers)
print(n)














# From below list create a new list with unique elements:
numbers = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
n=set(numbers)
print(n)

# Create a set from a list and remove 'name' if it is present in the set
numbers2 = [34, 123, 4, 34, 'name', 54]
numbers2.remove('name')
print(numbers2)
n=set([34, 123, 4, 34, 54])
print(n)


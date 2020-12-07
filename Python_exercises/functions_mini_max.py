"""Write a Python function to find the Min of three numbers."""

def min_three(x,y,z):
    args=x,y,z
    for i in args:
        return min(args)
print(min_three(9,-8,5))

#max
def max_three(x,y,z):
    args=x,y,z
    for i in args:
        return max(args)
print(max_three(9,-8,5))
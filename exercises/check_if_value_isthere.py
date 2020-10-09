"""check if 200 is in the dictionary"""

sampleDict = {'a': 100, 'b': 200, 'c': 300}

#var1
def isthere(num, desired_n=200):
    return str(desired_n) in str(num)

print(isthere({'a': 100, 'b': 200, 'c': 300}))

#var2
sampleDict = {'a': 100, 'b': 200, 'c': 300}
print(500 in sampleDict.values())




""" Define a function that takes one integer argument and returns 
logical value true or false depending on if the integer is a prime."""

#create a list of numbers and if you find a prime no in that least, it should return true 


def is_prime(num, primes=(2)):
		return str(primes) in str(num)
print(is_prime([2, 3, 5, 7, 11, 13]))


"""dictionary exercise 7: Check if a value 200 exists in a dictionary"""
def is_there(num, dict=(200)):
	return str(dict) in str(num)
print (is_there({'a': 100, 'b': 200, 'c': 300}))

"""make it a class"""

class x:
	def __init__(self, num, sample_d):
		self.num=num
		self.sample_d=sample_d
	
	def d(self,num,sample_d):
		return str(sample_d) in str(num)
	
	result=x({'a': 100, 'b': 200, 'c': 300})
	print(result.d())









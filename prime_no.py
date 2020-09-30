""" Define a function that takes one integer argument and returns 
logical value true or false depending on if the integer is a prime."""

#create a list of numbers and if you find a prime no in that least, it should return true 


def is_prime(num, primes=(2)):
		return str(primes) in str(num)
print(is_prime([2, 3, 5, 7, 11, 13]))


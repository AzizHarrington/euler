"""Project Euler Problem 3"""

def checker(x):
	if x == 1:
		return False
	if x == 2:
		return True
	for num in range(3, int(x**0.5)+1, 2):
		if x % num == 0:
			return False
	return True

def find_primes(x):
	primes = []
	for num in range(3, int(x**0.5)+1, 2):
		if checker(num):
			primes.append(num)
	return primes

def find_prime_factors(x):
	primes = find_primes(x)
	factors = []
	for prime in primes:
		if x % prime == 0:
			factors.append(prime)
	return factors

def find_max(x):
	return max(x)

primes = find_prime_factors(600851475143)

print find_max(primes)


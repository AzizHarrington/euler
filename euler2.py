
def fibo(n):
	current = 0
	prior = 1

	result = 0
	while current < n:
		current = current + prior
		prior = current - prior
		if current % 2 == 0:
			result = result + current
		
	return result


print fibo(4000000)


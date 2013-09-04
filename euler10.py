##The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##
##Find the sum of all the primes below two million.

def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True



def sum_primes(limit):
    total = 2
    i = 3
    while i < limit:
        if is_prime(i):
            total += i
        i += 2
    return total



print sum_primes(1000000)


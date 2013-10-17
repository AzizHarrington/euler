##A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
##
##a**2 + b**2 = c**2
##For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
##
##There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##Find the product abc.


def is_triplet(a, b, c):
    return a**2 + b**2 == c**2


#print is_triplet(3, 4, 5)

def find_triplets(n):
    for x in xrange(1, n):
        for y in xrange(x + 1, n):
            for z in xrange(y + 1, n):
                if is_triplet(x, y, z) == True and (x + y + z) == n:
                    return z * y * x
    return None

print find_triplets(1000)

def checker(n):
    if type(n) != str:
        n = str(n)
    if n == '':
        return True
    if n[0] != n[-1]:
        return False
    else:
        return checker(n[1:-1])

print checker(1001)


def largest_palindrome_number():
    largest = 0
    i = 900
    k = 900
    while i < 1000:
        while k < 1000:
            product = i * k
            if checker(product) and product > largest:
                largest = product
            k += 1
        k = 900
        i += 1
    return largest

print largest_palindrome_number()

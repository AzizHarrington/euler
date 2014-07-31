
def checker(i, x, y):
    for num in range(x, y + 1):
        if i % num != 0:
            return False
    return True

def find_smallest(start, x, y):
    i = start
    while not checker(i, x, y):
        i += start
    return i


print find_smallest(20, 11, 20)

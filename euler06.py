def sum_squares(x):
    sums = 0
    for num in range(1, x + 1):
        sums += num**2
    return sums

def square_sum(x):
    sums = 0
    for num in range(1, x + 1):
        sums += num
    return sums ** 2




print square_sum(100) - sum_squares(100)


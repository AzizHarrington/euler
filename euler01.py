def multiples(n):
    nums = []

    for num in range(0, n):
        if num % 3 == 0 or num % 5 == 0:
            nums.append(num)

    total = 0
    for element in nums:
        total += element

    return total

print multiples(1000)
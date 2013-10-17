#Project euler number 7

def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

#print is_prime(9)

def find_nth_prime(number):
    count = 0
    i = 1
    while count < number:
        if is_prime(i) == True:
            count += 1
            print i, count
            if count == number:
                return i
        i += 2
    return None


#print find_nth_prime(6)


print find_nth_prime(10001)



10001
##==> 104743 after 30 seconds
        
    

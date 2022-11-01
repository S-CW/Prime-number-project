"""Prime number is a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)."""

def is_prime(num):
    if num <= 1:
        return False
    else:
        for n in range(2, num):
            if num % n == 0:
                return False
        return True
    
def sum_of_prime(nums):
    return sum([x for x in nums if is_prime(x)])
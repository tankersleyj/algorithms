#  MIT (c) jtankersley 2019-05-18
from src import timer
import math


def is_prime(n):
    # return Boolean, Divisor
    if n == 1:
        return True, n
    if n % 2 == 0:
        return False, 2
    for i in range(3, round(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False, i
    return True, n


def get_primes(start, end):
    count_primes = 0
    for i in range(start, end + 1):
        prime, divisor = is_prime(i)
        if prime:
            count_primes += 1
            print(f"{i} is prime")
        # else:
            # print(f"{i} divisible by {divisor}")
    return count_primes

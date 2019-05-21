#  MIT (c) jtankersley 2019-05-18
from src import timer


def is_prime(n):
    if n == 1:
        return True
    if n == 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

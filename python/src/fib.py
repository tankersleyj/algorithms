#  MIT (c) jtankersley 2019-05-18
from src import timer


def get_fib_recursive(n):
    # return fib via recursive function ([0,1,1,2,3,5,8,13,26,39,etc.])
    if n < 1:
        return 0
    if n == 1:
        return 1
    return get_fib_recursive(n - 1) + get_fib_recursive(n - 2)


def get_fib_array(n):
    # return fib via array ([0,1,1,2,3,5,8,13,21,34,etc.])
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n - 1] + fib[n - 2]


def get_fib_vars(n):
    # return fib via loop and vars ([0,1,1,2,3,5,8,13,21,34,etc.])
    n_m1 = 0
    n_m2 = 1
    if n > 1:
        for i in range(2, n):
            n_m0 = n_m1
            n_m1 = n_m2
            n_m2 = n_m2 + n_m0
    return n_m1 + n_m2

def get_fib_var2(n):
    # return fib via loop & vars compact ([0,1,1,2,3,5,8,13,21,34,etc.])
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

#  MIT (c) jtankersley 2019-05-18
from src import timer


def getFib_recursive(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return getFib_recursive(n - 1) + getFib_recursive(n - 2)


def getFib_array(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n - 1] + fib[n - 2]


def getFib_vars(n):
    n_m1 = 0
    n_m2 = 1
    if n > 1:
        for i in range(2, n):
            n_m0 = n_m1
            n_m1 = n_m2
            n_m2 = n_m2 + n_m0
    return n_m1 + n_m2

def getFib_var2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

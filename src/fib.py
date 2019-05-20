# MIT (c) jtankersley 2019-05-18


def fib_for(n):
    n_m1 = 0
    n_m2 = 1
    if n > 1:
        for i in range(2, n):
            n_m0 = n_m1
            n_m1 = n_m2
            n_m2 = n_m2 + n_m0
    return n_m1 + n_m2


def print_fib_for(n):
    print(f"fib_for({n})={fib_for(n)}")


def fib_rec(n):
    if n < 0:
        return 0
    if n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


def print_fib_rec(n):
    print(f"fib_rec({n})={fib_rec(n)}")

def fib_for(n):
    n_m1 = 0
    n_m2 = 1
    if n > 1:
        for i in range(2, n):
            n_m0 = n_m1
            n_m1 = n_m2
            n_m2 = n_m2 + n_m0
    return n_m1 + n_m2


def fib_rec(n):
    if n < 0:
        return 0
    if n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


def execute():
    for i in range(1, 10):
        print(f"fib_for({i})={fib_for(i)}")
    for i in range(1, 10):
        print(f"fib_rec({i})={fib_rec(i)}")

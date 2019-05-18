def is_prime(n):
    if n == 1:
        return True
    if n == 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
              #     print(f"{n} % {i} == 0")
            return False
    return True


def execute():
    for i in range(12):
        print(f"is_prime({i})={is_prime(i)})")

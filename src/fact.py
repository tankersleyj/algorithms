import math

def is_factorial(n):
  f = 1
  i = 0
  while f < n:
    i += 1
    f *= i
    if f == n:
      print(f"result: {i}! == {n}")
    else:
      print(f"check: {i}! == {f}")

def get_factors(n):
  factors = []
  for i in range(1, n):
    if n % i == 0:
      factors.append(i)
  print(f"factors of {n} = {factors}")
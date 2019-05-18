# MIT, jtankersley, 2019-05-18
import math

def is_factorial(n):
  f = 1
  i = 0
  result = False
  while f < n:
    i += 1
    f *= i
    if f == n:
      result = True
      break
  return result

def print_is_factorial(n):
  print(f"is_factorial({n}) = {is_factorial(n)}")

def get_factors(n):
  factors = []
  for i in range(1, n):
    if n % i == 0:
      factors.append(i)
  return factors

def print_get_factors(n):
  print(f"factors of {n} = {get_factors(n)}")

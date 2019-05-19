# MIT (c) jtankersley 2019-05-18
import math
from . import timer

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


@timer.timeit
def print_is_factorial(n):
  print(f"is_factorial({n}) = {is_factorial(n)}")

def get_factors(n):
  factors = []
  for i in range(1, n):
    if n % i == 0:
      factors.append(i)
  return factors


@timer.timeit
def print_get_factors(n, log_time={}):
  print(f"factors of {n} = {get_factors(n)}")

def get_factorial(n):
  result = 0
  if n > 0:
    result = 1
  if n > 1:
    for i in range(2, n):
      result *= i
  return result


@timer.timeit
def print_get_factorial(n):
  print(f"get_factorial({n}) = {get_factorial(n)}")

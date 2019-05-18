# MIT, jtankersley, 2019-05-18

import sys
from . import command
from . import fib
from . import prime
from . import fact

def execute():
  cmd = command.Command()
  if cmd.equal("fib_for"):
    fib.print_fib_for(int(cmd.arg(2, 10)))
  if cmd.equal("fib_rec"):
    fib.print_fib_rec(int(cmd.arg(2, 10)))
  if cmd.equal("is_prime"):
    prime.print_is_prime(int(cmd.arg(2, 11)))
  if cmd.equal("is_factorial"):
    fact.print_is_factorial(int(cmd.arg(2, 87178291200)))
  if cmd.equal("get_factors"):
    fact.print_get_factors(int(cmd.arg(2, 121)))
  if len(cmd.command()) == 0:
    cmd.get_help()

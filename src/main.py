# MIT, jtankersley, 2019-05-18

import sys
from . import app
from . import fib
from . import prime
from . import fact

def execute():
  cmd = app.command()
  if cmd.equal("fib"):
    fib.execute()
  if cmd.equal("prime"):
    prime.execute()
  if cmd.equal("fact"):
    fact.is_factorial(87178291200)
    fact.get_factors(121)
  # fact.get_factors(87178291200)
  if len(cmd.command()) == 0:
    print(f"options: {cmd.commands()}")

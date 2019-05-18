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
  if cmd.equal("is_fact"):
    fact.is_factorial(int(cmd.arg(2, 87178291200)))
  if cmd.equal("get_fact"):
    fact.get_factors(int(cmd.arg(2, 121)))
  if len(cmd.command()) == 0:
    print(f"  options: {cmd.commands()}")
    print(f"  example: ./run.sh is_fact 40302")

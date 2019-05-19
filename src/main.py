# MIT (c) jtankersley 2019-05-18

import sys
from . import arg
from . import fact
from . import fib
from . import prime
from . import sort

def execute():
  cmd = arg.CommandHandler()
  if cmd.is_command("fib_for"):
    fib.print_fib_for(int(cmd.arg(2, 10)))
  if cmd.is_command("fib_rec"):
    fib.print_fib_rec(int(cmd.arg(2, 10)))
  if cmd.is_command("get_factors"):
    fact.print_get_factors(int(cmd.arg(2, 121)))
  if cmd.is_command("get_factorial"):
    fact.print_get_factorial(int(cmd.arg(2, 10)))
  if cmd.is_command("is_factorial"):
    fact.print_is_factorial(int(cmd.arg(2, 87178291200)))
  if cmd.is_command("is_prime"):
    prime.print_is_prime(int(cmd.arg(2, 11)))
  if cmd.is_command("sort_bubble"):
    sort.print_sort_bubble()
  if cmd.is_command("sort_instant"):
    sort.print_sort_instant()
  if cmd.is_command("sort_merge"):
    sort.print_sort_merge()
  if cmd.is_command("sort_quick"):
    sort.print_sort_quick()
  if not cmd.is_handled():
    cmd.get_help(
      "---- CS Algorithms in Python, MIT, (c) 2019, JTankersley ----",
      "./run.sh get_factors 40302"
    )

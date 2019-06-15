#  MIT (c) jtankersley 2019-05-18

import sys
from src import args
from src import base
from src import fact
from src import fib
from src import prime
from src import search
from src import sort
from src import timer

orderedList = "1,2,3,4,5,6,7,8,10,12,15,20,25,30,31,32"
unOrderedList = "10,20,31,4,6,5,15,2,12,25,3,30,32,1,7,8"


def execute():
    cmd = args.CommandHandler()
    if cmd.is_command("convert_from_base_10"):
        timer.run_timed_result(
            base.convert_from_base_10, 
            cmd.arg(2, "27"), 
            int(cmd.arg(3, "2"))
        )
    if cmd.is_command("convert_to_base_10"):
        timer.run_timed_result(
            base.convert_to_base_10, 
            cmd.arg(2, "11011"), 
            int(cmd.arg(3, "2"))
        )
    if cmd.is_command("get_fib_recursive"):
       timer.run_timed_result(
            fib.get_fib_recursive, 
            int(cmd.arg(2, "16"))
        )    
    if cmd.is_command("get_fib_array"):
        timer.run_timed_result(
            fib.get_fib_array, 
            int(cmd.arg(2, "16"))
        )
    if cmd.is_command("get_fib_vars"):
        timer.run_timed_result(
            fib.get_fib_vars, 
            int(cmd.arg(2, "16"))
        )
    if cmd.is_command("get_fib_var2"):
        timer.run_timed_result(
            fib.get_fib_var2, 
            int(cmd.arg(2, "16"))
        )
    if cmd.is_command("get_factors"):
        timer.run_timed_result(
            fact.get_factors,
            int(cmd.arg(2, "121"))
        )
    if cmd.is_command("get_factorial"):
        timer.run_timed_result(
            fact.get_factorial,
            int(cmd.arg(2, "10"))
        )
    if cmd.is_command("is_factorial"):
        timer.run_timed_result(
            fact.is_factorial,
            int(cmd.arg(2, "87178291200"))
        )
    if cmd.is_command("is_prime"):
        timer.run_timed_result(
            prime.is_prime,
            int(cmd.arg(2, "11"))
        )
    if cmd.is_command("get_primes"):
        timer.run_timed_result(
            prime.get_primes,
            int(cmd.arg(2, "9999999900")),
            int(cmd.arg(3, "9999999999")),
            bool(cmd.arg(4, False))
        )
    if cmd.is_command("binary_search"):
        timer.run_timed_result(
            search.binary_search,
            cmd.arg(2, orderedList).split(","),
            cmd.arg(3, "10")
        )
    if cmd.is_command("bubble_sort"):
        timer.run_timed_result(
            sort.print_bubble_sort,
            cmd.arg(2, unOrderedList).split(",")
        )
    if cmd.is_command("merge_sort"):
        timer.run_timed_result(
            sort.merge_sort,
            cmd.arg(2, unOrderedList).split(",")
        )
    if cmd.is_command("python_sort"):
        timer.run_timed_result(
            sort.python_sort,
            cmd.arg(2, unOrderedList).split(",")
        )
    if not cmd.is_handled():
        help_text = cmd.get_help(
            "---- CS Algorithms in Python, MIT, (c) 2019, JTankersley ----",
            "run <function> [<value>]",
            "./run.sh get_factors 40302"
        )
        print(f"{help_text}")

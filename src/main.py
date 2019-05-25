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
    if cmd.is_command("fib_recursive"):
       timer.run_timed_result(
            fib.fib_recursive, 
            int(cmd.arg(2, 16))
        )    
    if cmd.is_command("fib_array"):
        timer.run_timed_result(
            fib.fib_array, 
            int(cmd.arg(2, 16))
        )
    if cmd.is_command("fib_vars"):
        timer.run_timed_result(
            fib.fib_vars, 
            int(cmd.arg(2, 16))
        )
    if cmd.is_command("get_factors"):
        timer.run_timed_result(
            fact.get_factors,
            int(cmd.arg(2, 121))
        )
    if cmd.is_command("get_factorial"):
        timer.run_timed_result(
            fact.get_factorial,
            int(cmd.arg(2, 10))
        )
    if cmd.is_command("is_factorial"):
        timer.run_timed_result(
            fact.is_factorial,
            int(cmd.arg(2, 87178291200))
        )
    if cmd.is_command("is_prime"):
        timer.run_timed_result(
            prime.is_prime,
            int(cmd.arg(2, 11))
        )
    if cmd.is_command("search_binary"):
        timer.run_timed_result(
            search.search_binary
        )
    if cmd.is_command("search_hash"):
        timer.run_timed_result(
            search.search_hash
        )
    if cmd.is_command("search_tree"):
        timer.run_timed_result(
            search.search_tree
        )
    if cmd.is_command("sort_instant"):
        timer.run_timed_result(
            sort.print_sort_instant
        )
    if cmd.is_command("sort_merge"):
        timer.run_timed_result(
            sort.print_sort_merge
        )
    if cmd.is_command("sort_quick"):
        timer.run_timed_result(
            sort.print_sort_quick
        )
    if not cmd.is_handled():
        help_text = cmd.get_help(
            "---- CS Algorithms in Python, MIT, (c) 2019, JTankersley ----",
            "run <function> [<value>]",
            "./run.sh get_factors 40302"
        )
        print(f"{help_text}")

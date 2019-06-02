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

ordered_list = "1,2,3,4,5,6,7,8,10,12,15,20,25,30,31,32"
unordered_list = "10,20,31,4,6,5,15,2,12,25,3,30,32,1,7,8"


def execute():
    cmd = args.CommandHandler()
    if cmd.isCommand("convert_from_base_10"):
        timer.runTimedResult(
            base.convert_from_base_10, 
            cmd.arg(2, "27"), 
            int(cmd.arg(3, "2"))
        )
    if cmd.isCommand("convert_to_base_10"):
        timer.runTimedResult(
            base.convert_to_base_10, 
            cmd.arg(2, "11011"), 
            int(cmd.arg(3, "2"))
        )
    if cmd.isCommand("fib_recursive"):
       timer.runTimedResult(
            fib.fib_recursive, 
            int(cmd.arg(2, "16"))
        )    
    if cmd.isCommand("fib_array"):
        timer.runTimedResult(
            fib.fib_array, 
            int(cmd.arg(2, "16"))
        )
    if cmd.isCommand("fib_vars"):
        timer.runTimedResult(
            fib.fib_vars, 
            int(cmd.arg(2, "16"))
        )
    if cmd.isCommand("fib_var2"):
        timer.runTimedResult(
            fib.fib_var2, 
            int(cmd.arg(2, "16"))
        )
    if cmd.isCommand("get_factors"):
        timer.runTimedResult(
            fact.get_factors,
            int(cmd.arg(2, "121"))
        )
    if cmd.isCommand("get_factorial"):
        timer.runTimedResult(
            fact.get_factorial,
            int(cmd.arg(2, "10"))
        )
    if cmd.isCommand("is_factorial"):
        timer.runTimedResult(
            fact.is_factorial,
            int(cmd.arg(2, "87178291200"))
        )
    if cmd.isCommand("is_prime"):
        timer.runTimedResult(
            prime.is_prime,
            int(cmd.arg(2, "11"))
        )
    if cmd.isCommand("search_binary"):
        timer.runTimedResult(
            search.search_binary,
            cmd.arg(2, ordered_list).split(","),
            cmd.arg(3, "10")
        )
    if cmd.isCommand("sort_bubble"):
        timer.runTimedResult(
            sort.print_sort_bubble,
            cmd.arg(2, unordered_list).split(",")
        )
    if cmd.isCommand("sort_merge"):
        timer.runTimedResult(
            sort.sort_merge,
            cmd.arg(2, unordered_list).split(",")
        )
    if cmd.isCommand("sort_python"):
        timer.runTimedResult(
            sort.sort_python,
            cmd.arg(2, unordered_list).split(",")
        )
    if not cmd.isHandled():
        help_text = cmd.getHelp(
            "---- CS Algorithms in Python, MIT, (c) 2019, JTankersley ----",
            "run <function> [<value>]",
            "./run.sh get_factors 40302"
        )
        print(f"{help_text}")

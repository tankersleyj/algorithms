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
    if cmd.isCommand("convertFromBase10"):
        timer.runTimedResult(
            base.convertFromBase10, 
            cmd.arg(2, "27"), 
            int(cmd.arg(3, "2"))
        )
    if cmd.isCommand("convertToBase10"):
        timer.runTimedResult(
            base.convertToBase10, 
            cmd.arg(2, "11011"), 
            int(cmd.arg(3, "2"))
        )
    if cmd.isCommand("getFib_recursive"):
       timer.runTimedResult(
            fib.getFib_recursive, 
            int(cmd.arg(2, "16"))
        )    
    if cmd.isCommand("getFib_array"):
        timer.runTimedResult(
            fib.getFib_array, 
            int(cmd.arg(2, "16"))
        )
    if cmd.isCommand("getFib_vars"):
        timer.runTimedResult(
            fib.getFib_vars, 
            int(cmd.arg(2, "16"))
        )
    if cmd.isCommand("getFib_var2"):
        timer.runTimedResult(
            fib.getFib_var2, 
            int(cmd.arg(2, "16"))
        )
    if cmd.isCommand("getFactors"):
        timer.runTimedResult(
            fact.getFactors,
            int(cmd.arg(2, "121"))
        )
    if cmd.isCommand("getFactorial"):
        timer.runTimedResult(
            fact.getFactorial,
            int(cmd.arg(2, "10"))
        )
    if cmd.isCommand("isFactorial"):
        timer.runTimedResult(
            fact.isFactorial,
            int(cmd.arg(2, "87178291200"))
        )
    if cmd.isCommand("isPrime"):
        timer.runTimedResult(
            prime.isPrime,
            int(cmd.arg(2, "11"))
        )
    if cmd.isCommand("binarySearch"):
        timer.runTimedResult(
            search.binarySearch,
            cmd.arg(2, orderedList).split(","),
            cmd.arg(3, "10")
        )
    if cmd.isCommand("bubbleSort"):
        timer.runTimedResult(
            sort.print_bubbleSort,
            cmd.arg(2, unOrderedList).split(",")
        )
    if cmd.isCommand("mergeSort"):
        timer.runTimedResult(
            sort.mergeSort,
            cmd.arg(2, unOrderedList).split(",")
        )
    if cmd.isCommand("pythonSort"):
        timer.runTimedResult(
            sort.pythonSort,
            cmd.arg(2, unOrderedList).split(",")
        )
    if not cmd.isHandled():
        help_text = cmd.getHelp(
            "---- CS Algorithms in Python, MIT, (c) 2019, JTankersley ----",
            "run <function> [<value>]",
            "./run.sh getFactors 40302"
        )
        print(f"{help_text}")

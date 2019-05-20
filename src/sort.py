#  MIT (c) jtankersley 2019-05-18
from src import timer


@timer.print_time_dec
def print_sort_bubble():
    print("merge")


@timer.print_time_dec
def print_sort_instant():
    print("merge")


@timer.print_time_dec
def print_sort_merge():
    print("merge")


@timer.print_time_dec
def print_sort_quick():
    print("quick")

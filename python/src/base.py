#  MIT (c) jtankersley 2019-05-18
import math


def _convert_number_to_char(number):
    char = "0"
    integer = int(number)
    if 0 <= integer <= 9:
        char = chr(integer + 48)  # number 0-9 = ascii 48-57 = 0-9
    elif 10 <= integer <= 35:
        char = chr(integer + 55)  # number 10-35 = ascii 65-90 = A-Z
    return char 


def _convert_char_to_number(char):
    ord_val = ord(char)
    number = 0
    if 48 <= ord_val <= 57:  # ascii 48-57 = char 0-9 = number 0-9
        number = ord_val - 48
    elif 65 <= ord_val <= 90:  # ascii 65-90 = char A-Z = number 10-35
        number = ord_val - 55
    return number 


def convert_to_base_10(string, from_base):
    # example: "11011",2 = 1*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0
    result =  0
    for index, char in enumerate(string):
        number = _convert_char_to_number(char) 
        exponent = len(string) - index - 1
        result += number * math.pow(from_base, exponent)
    return result


def convert_from_base_10(number, from_base):
    # example: 100,2 = (100 // 64) + ((100 % 64) // 32) + ((100 % 64) % 32) + (((100 % 64) % 32) % 16) // 8) ...
    # example: 100,16 = (100 % 16^1) + (100 - (100 % 16)) % 16^2 ...
    result =  ""
    left = int(number)
    index = 0
    base_exp = 0
    while base_exp < left:
        index += 1
        base_exp = math.pow(int(from_base), index)
    while left > 0:
        if base_exp <= left:
            char_num = left // base_exp
            result += _convert_number_to_char(char_num)
            left -= char_num * base_exp
        else:
            result += _convert_number_to_char(0)
        index -= 1
        base_exp = math.pow(int(from_base), index)
    return result

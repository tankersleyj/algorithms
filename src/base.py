#  MIT (c) jtankersley 2019-05-18
import math


def _convertNumberToChar(number):
    char = "0"
    integer = int(number)
    if 0 <= integer <= 9:
        char = chr(integer + 48)
    elif 10 <= integer <= 55:
        char = chr(integer + 55)
    return char 


def _convertCharToNumber(char):
    ord_val = ord(char)
    number = 0
    if 48 <= ord_val <= 57:
        number = ord_val - 48
    elif 65 <= ord_val <= 90:
        number = ord_val - 55
    return number 


def convertToBase10(string, base):
    # example: "11011",2 = 1*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0
    result =  0
    for index, char in enumerate(string):
        number = _convertCharToNumber(char) 
        exponent = len(string) - index - 1
        result += number * math.pow(base, exponent)
    return result


def convertFromBase10(number, base):
    # example: 100,2 = (100 // 64) + ((100 % 64) // 32) + ((100 % 64) % 32) + (((100 % 64) % 32) % 16) // 8) ...
    # example: 100,16 = (100 % 16^1) + (100 - (100 % 16)) % 16^2 ...
    result =  ""
    left = int(number)
    index = 0
    base_exp = 0
    while base_exp < left:
        index += 1
        base_exp = math.pow(int(base), index)
    while left > 0:
        if base_exp <= left:
            char_num = left // base_exp
            result += _convertNumberToChar(char_num)
            left -= char_num * base_exp
        else:
            result += _convertNumberToChar(0)
        index -= 1
        base_exp = math.pow(int(base), index)
    return result

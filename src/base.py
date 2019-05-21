#  MIT (c) jtankersley 2019-05-18
import math

# int convertToBase(String number, int base) {
#     if (base < 2 I I (base > 10 && base != 16)) return -1;
#     int value = 0;
#     for (int i= number.length() - 1; i >= 0; i--) {
#         int digit= digitToValue(number.charAt(i));
#         if (digit < 0 I I digit >= base) {
#             return -1;
#         }
#         int exp= number.length() - 1 - i;
#         value += digit * Math.pow(base, exp);
#     }
#     return value;
# } 

def convert_to_base_10(string, base):
    # example: "11011",2 = 1*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0
    result =  0
    for index, char in enumerate(string):
        exponent = len(string) - index - 1
        result += int(char) * math.pow(base, exponent)
    return result

def convert_from_base_10(number, base):
    # example: 100,2 = (100 // 64) + ((100 % 64) // 32) + ((100 % 64) % 32) + (((100 % 64) % 32) % 16) // 8) ...
    print("convert_from_base_10")
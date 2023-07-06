
from math import isqrt
from decimal import Decimal

def square_visual(number):
    if isinstance(number, float):
        precision = count_decimal_places(number)
        number_str = str(round(number, precision))
    else:
        number_str = str(number)
    side_length = isqrt(len(number_str))
   
    if side_length < 2:
        raise ValueError(number)
    # Create the square grid
    return [list(number_str[i:i + side_length]) for i in range(0, len(number_str) -1 , side_length)]



def count_decimal_places(num):
    return abs(Decimal(num).as_tuple().exponent)

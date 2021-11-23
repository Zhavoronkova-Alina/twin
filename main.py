import numpy as np
from mpmath import *
from twin import *
from intvalpy import Interval, precision


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a1 = 1
    a2 = 4
    b1 = 6
    b2 = 10

    data1 = Interval(a1, a2)
    data2 = Interval(b1, b2)
    data3 = Interval(a1, b1)
    data4 = Interval(a2, b2)

    tw1 = Twin(data1, data2)
    tw1.print()
    tw2 = Twin(data3, data4)
    tw2.print()

    twins_plus(tw1, tw2).print()

    twins_multiply(tw1, tw2).print()

    unary_minus_twin(tw1).print()

    inverse_twin(tw1).print()


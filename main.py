import numpy as np
from mpmath import *
from twin import *
from intvalpy import *
from operation import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a1 = None
    a2 = 4
    b1 = 6
    b2 = 10

    #float('nan')
    #data1 = Interval(1, 6)
    data1 = Interval(float('nan'), float('nan'))
    data2 = Interval(1, 10)
    #data3 = Interval(3, 5)
    data3 = Interval(float('nan'), float('nan'))
    data4 = Interval(2, 6)

    tw1 = Twin(data1, data2)
    print(tw1)
    tw2 = Twin(data3, data4)
    print(tw2)

    #print(p(tw1, tw2))
    #print(q(tw1, tw2))

    #print(psi(data1, data2))

    #print(twins_plus(tw1, tw2))

    print(twins_multiply(tw1, tw2))

    #print(unary_minus_twin(tw1))

    #print(inverse_twin(tw1))


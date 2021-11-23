from mpmath import *
from intvalpy import Interval, precision, intersection


class Twin(object):
    def __init__(self, a1, a2):
        # a1 and a2 must be a single intervals. If it have property "len", there are not single intervals
        if hasattr(a1, 'len') or hasattr(a2, 'len'):
            print("a1 or a2 is not single intervals. Check your data.")
            exit()

        if isnan(float(a2.a)) or isnan(float(a2.b)):
            print("The outer interval cannot be empty.")
            exit()

        self.int = a1

        if (isnan(float(a1.a)) or isnan(float(a1.b))) and a2.a == a2.b:
            self.int = a2

        self.out = a2

    def int_width(self):
        if isnan(self.int.a):
            return -1
        return self.int.wid

    def out_width(self):
        return self.out.wid

    def print(self):
        print("Twin([ ", self.int, ", ", self.out, " ])")


# T1 = ( [a-, a+], [A-, A+] )
# T2 = ( [b-, b+], [B-, B+] )

def p(T1: Twin, T2: Twin):
    if T1.int_width() == -1 and T2.int_width() == -1:
        return None

    if T1.int_width() == -1:
        return T2.int.a + T1.out.b

    if T2.int_width() == -1:
        return T1.int.a + T2.out.b

    return min(T1.int.a + T2.out.b, T2.int.a + T1.out.b)


def q(T1: Twin, T2: Twin):
    if T1.int_width() == -1 and T2.int_width() == -1:
        return None

    if T1.int_width() == -1:
        return T2.int.b + T1.out.a

    if T2.int_width() == -1:
        return T1.int.b + T2.out.a

    return max(T1.int.b + T2.out.a, T2.int.b + T1.out.a)


def twins_plus(T1: Twin, T2: Twin):
    if T1.out_width() <= T2.int_width() or T2.out_width() <= T1.int_width():
        return Twin(
            Interval(p(T1, T2), q(T1, T2)),
            Interval(T1.out.a + T2.out.a, T1.out.b + T2.out.b)
        )
    else:
        return Twin(
            Interval(None, None),
            Interval(T1.out.a + T2.out.a, T1.out.b + T2.out.b)
        )


def phi(I1, I2):
    Z = intersection(I1, I2)

    if not (isnan(float(Z.a)) or isnan(float(Z.b))):
        return Interval(None, None)
    elif not isnan(float(Z.a)) and (not isnan(float(Z.b))) and Z.a != Z.b:
        return Interval(None, None)
    else:
        min_ = abs(I1.a - I2.a)
        min_a = I1.a
        min_b = I2.a

        if abs(I1.b - I2.b) < min_:
            min_ = abs(I1.b - I2.b)
            min_a = I1.b
            min_b = I2.b

        if abs(I1.a - I2.b) < min_:
            min_ = abs(I1.a - I2.b)
            min_a = I1.a
            min_b = I2.b

        if abs(I1.b - I2.a) < min_:
            min_ = abs(I1.b - I2.a)
            min_a = I1.b
            min_b = I2.a

        return Interval(min_a, min_b)


def psi(I1, I2):
    return Interval(
        min(I1.a, I1.b, I2.a, I2.b),
        max(I1.a, I1.b, I2.a, I2.b)
    )


# T1 = ( [a-, a+], [A-, A+] )
# T2 = ( [b-, b+], [B-, B+] )
def twins_multiply(T1: Twin, T2: Twin):
    if T1.int_width() == -1 and T2.int_width() == -1:
        return Twin(
            Interval(None, None),
            Interval(T1.out.a, T1.out.b) * Interval(T2.out.a, T2.out.b)
        )

    if T1.int_width() == -1:
        return Twin(
            phi(
                T2.int.a * Interval(T1.out.a, T1.out.b),
                T2.int.b * Interval(T1.out.a, T1.out.b)
            ),
            Interval(T1.out.a, T1.out.b) * Interval(T2.out.a, T2.out.b)
        )

    if T2.int_width() == -1:
        return Twin(
            phi(
                T1.int.a * Interval(T2.out.a, T2.out.b),
                T1.int.b * Interval(T2.out.a, T2.out.b)
            ),
            Interval(T1.out.a, T1.out.b) * Interval(T2.out.a, T2.out.b)
        )

    return Twin(
        psi(
            phi(
                mpf(T1.int.a) * Interval(T2.out.a, T2.out.b),
                mpf(T1.int.b) * Interval(T2.out.a, T2.out.b)
            ),
            phi(
                T2.int.a * Interval(T1.out.a, T1.out.b),
                T2.int.b * Interval(T1.out.a, T1.out.b)
            )
        ),
        Interval(T1.out.a, T1.out.b) * Interval(T2.out.a, T2.out.b)
    )


def unary_minus_twin(T: Twin):
    return Twin(-T.int, -T.out)


def inverse_twin(T: Twin):
    if 0 in T.int or 0 in T.out:
        print("Cannot be divided into intervals containing 0.")
        exit()

    return Twin(1 / T.int, 1 / T.out)


def is_twins_equal(T1: Twin, T2: Twin):
    if T1.int.a == T2.int.a and T1.int.b == T2.int.b and T1.out.a == T2.out.a and T1.out.b == T2.out.b:
        return True
    else:
        return False


def is_twins_leq(T1: Twin, T2: Twin):
    if (T1.out in T2.out) and (T2.int in T1.int):
        return True
    else:
        return False

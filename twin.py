from mpmath import *
from intvalpy import Interval, precision, intersection


class Twin(object):
    def __init__(self, X_l, X):
        # I1 and I2 must be a single intervals. If it have property "len", there are not single intervals
        if hasattr(X_l, 'len') or hasattr(X, 'len'):
            print("I1 or I2 is not single intervals. Check your data.")
            exit()

        if isnan(float(X.a)) or isnan(float(X.b)):
            print("The outer interval cannot be empty.")
            exit()

        self.X_l = X_l

        if (isnan(float(X_l.a)) or isnan(float(X_l.b))) and X.a == X.b:
            self.X_l = X

        self.X = X

        if isnan(self.X_l.a):
            self.X_l_width = -1
        else:
            self.X_l_width = self.X_l.wid

        self.X_width = self.X.wid

    def __str__(self):
        return "[" + str(self.X_l) + ", " + str(self.X) + "]"

# T1 = ( [a-, a+], [A-, A+] )
# T2 = ( [b-, b+], [B-, B+] )

def p(T1: Twin, T2: Twin):
    if T1.X_l_width == -1 and T2.X_l_width == -1:
        return float('nan')

    if T1.X_l_width == -1:
        return T2.X_l.a + T1.X.b

    if T2.X_l_width == -1:
        return T1.X_l.a + T2.X.b

    return min(T1.X_l.a + T2.X.b, T2.X_l.a + T1.X.b)


def q(T1: Twin, T2: Twin):
    if T1.X_l_width == -1 and T2.X_l_width == -1:
        return float('nan')

    if T1.X_l_width == -1:
        return T2.X_l.b + T1.X.a

    if T2.X_l_width == -1:
        return T1.X_l.b + T2.X.a

    return max(T1.X_l.b + T2.X.a, T2.X_l.b + T1.X.a)


def twins_plus(T1: Twin, T2: Twin):
    if T1.X_width <= T2.X_l_width or T2.X_width <= T1.X_l_width:
        return Twin(
            Interval(p(T1, T2), q(T1, T2)),
            Interval(T1.X.a + T2.X.a, T1.X.b + T2.X.b)
        )
    else:
        return Twin(
            Interval(float('nan'), float('nan')),
            Interval(T1.X.a + T2.X.a, T1.X.b + T2.X.b)
        )


def phi(I1, I2):
    Z = intersection(I1, I2)

    if not (isnan(float(Z.a)) or isnan(float(Z.b))):
        return Interval(float('nan'), float('nan'))
    elif not isnan(float(Z.a)) and (not isnan(float(Z.b))) and Z.a != Z.b:
        return Interval(float('nan'), float('nan'))
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
    if T1.X_l_width == -1 and T2.X_l_width == -1:
        return Twin(
            Interval(float('nan'), float('nan')),
            Interval(T1.X.a, T1.X.b) * Interval(T2.X.a, T2.X.b)
        )

    if T1.X_l_width == -1:
        return Twin(
            phi(
                T2.X_l.a * Interval(T1.X.a, T1.X.b),
                T2.X_l.b * Interval(T1.X.a, T1.X.b)
            ),
            Interval(T1.X.a, T1.X.b) * Interval(T2.X.a, T2.X.b)
        )

    if T2.X_l_width == -1:
        return Twin(
            phi(
                T1.X_l.a * Interval(T2.X.a, T2.X.b),
                T1.X_l.b * Interval(T2.X.a, T2.X.b)
            ),
            Interval(T1.X.a, T1.X.b) * Interval(T2.X.a, T2.X.b)
        )

    return Twin(
        psi(
            phi(
                (T1.X_l.a) * Interval(T2.X.a, T2.X.b),
                (T1.X_l.b) * Interval(T2.X.a, T2.X.b)
            ),
            phi(
                T2.X_l.a * Interval(T1.X.a, T1.X.b),
                T2.X_l.b * Interval(T1.X.a, T1.X.b)
            )
        ),
        Interval(T1.X.a, T1.X.b) * Interval(T2.X.a, T2.X.b)
    )


def unary_minus_twin(T: Twin):
    return Twin(-T.X_l, -T.X)


def inverse_twin(T: Twin):
    if 0 in T.X_l or 0 in T.X:
        print("Cannot be divided into intervals containing 0.")
        exit()

    return Twin(1 / T.X_l, 1 / T.X)


def is_twins_equal(T1: Twin, T2: Twin):
    if T1.X_l.a == T2.X_l.a and T1.X_l.b == T2.X_l.b and T1.X.a == T2.X.a and T1.X.b == T2.X.b:
        return True
    else:
        return False


def is_twins_leq(T1: Twin, T2: Twin):
    if (T1.X in T2.X) and (T2.X_l in T1.X_l):
        return True
    else:
        return False

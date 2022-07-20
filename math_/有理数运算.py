import decimal
from decimal import *
from fractions import Fraction


def main1(name):
    decimal.getcontext().prec = 100
    print(Decimal(2) / Decimal(7))
    # print(f'Hi, {name}')


def main2():
    n1 = Fraction(2, 7)
    # print(n1)
    n2 = Fraction(3, 7)
    print(n1 + n2)
    # print(n1.numerator)


def main3():
    print(int(3**40/3))

    from fractions import Fraction
    print(Fraction(3**40, 3).numerator)


if __name__ == '__main__':
    # print([int(Fraction(1))])
    main3()

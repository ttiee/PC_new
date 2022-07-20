from sympy import *


def jie(a, b):
    x = symbols('x')
    y = symbols('y')
    return solve([Eq(x+y, a), Eq(x-y, b)], [x, y])


def jie1(a, b, c):
    x = symbols('x')
    print(solve(a*x**2 + b*x + c, x))


def no():
    x = symbols('x')
    print(solve([x - 1, x + 1], x))


if __name__ == '__main__':
    no()
    # print(jie(2, 0))
    # jie1(1, -2, 1)


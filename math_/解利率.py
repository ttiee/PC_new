from sympy import *


def jie():
    r = symbols('r')
    c = symbols('c')
    i = symbols('i')
    g = symbols('g')
    y = symbols('y')
    p = symbols('p')
    M = symbols('M')
    W = symbols('W')
    N = symbols('N')
    equations = [Eq(c, 90 + 0.8 * (y - 100)),
                 Eq(i, 150 - 6 * r),
                 Eq(g, 100),
                 Eq(y, c + i + g),
                 # Eq(160 / p, 0.2 * y - 4 * r),
                 Eq(M / p, 0.2 * y - 4 * r),
                 Eq(M, 160),
                 ]
    equations1 = [
                 Eq(N, 175 - 12.5 * W / p),
                 Eq(N, 70 + W),
                 Eq(y, -N ** 2 / 25 + 14 * N),
                 ]
    e1 = solve(equations1, [y, W, N])[0][0]
    e2 = solve(equations, [y, r, c, g, i, M])[y]
    print(e1, '\n', e2)
    return solve([Eq(y, e1), Eq(y, e2)], [p, y])


def jie1():
    r = symbols('r')
    c = symbols('c')
    i = symbols('i')
    g = symbols('g')
    y = symbols('y')
    p = symbols('p')
    M = symbols('M')
    W = symbols('W')
    N = symbols('N')
    equations = [
        Eq(c, 90 + 0.8 * (y - 100)),
        Eq(i, 150 - 6 * r),
        Eq(g, 100),
        Eq(y, c + i + g),
        # Eq(160 / p, 0.2 * y - 4 * r),
        Eq(M / p, 0.2 * y - 4 * r),
        Eq(M, 160),
        Eq(N, 175 - (12.5 * W) / p),
        Eq(N, 70 + W),
        Eq(y, -(N ** 2) / 25 + 14 * N),
        ]

    return solve(equations, [p, y, r, c, g, i, M, N, W])


def jie2():
    r = symbols('r')
    c = symbols('c')
    i = symbols('i')
    g = symbols('g')
    y = symbols('y')
    p = symbols('p')
    M = symbols('M')
    W = symbols('W')
    N = symbols('N')
    equations = [
        Eq(c, 90 + 0.8 * (y - 100)),
        Eq(i, 150 - 6 * r),
        Eq(g, 100),
        Eq(y, c + i + g),
        # Eq(160 / p, 0.2 * y - 4 * r),
        Eq(M / p, 0.2 * y - 4 * r),
        Eq(M, 160),
        Eq(N, 175 - (12.5 * W) / p),
        Eq(N, 70 + 5*W),
        Eq(y, -(N ** 2) * 0.04 + 14 * N),
        ]

    return solve(equations, [p, y, r, c, g, i, M, N, W])


if __name__ == '__main__':
    # print(jie())
    print(jie2())

from sympy import *

x = symbols('x')

print(solve(-((-75/x+175)**2)/25+14*(-75/x+175)-520-480/x, x))

# f1 = x**3 + x**2 + 6
# f1_ = diff(f1, x)
# print(f1_)

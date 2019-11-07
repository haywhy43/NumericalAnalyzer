import random
from Newton import newton
from Secant import secant
from Bisection import bisection
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = (standard_transformations + (implicit_multiplication_application,))

x = Symbol('x')
method = input("Please enter the method you want to use in lowercase: ")
f = eval(input("Please input the order of the equation(i.e the highest power in the polynomial): "))
coefficient = []

for i in range(f + 1):
    coefficient.append(input("Enter Coefficient of order " + format(i) + ": "))

coefficient.reverse()
fx = ''
for j in range(len(coefficient)):
    fx = fx + " " + str(coefficient[j]) + "*x ** " + str(len(coefficient) - (j + 1)) + " + "

fx = fx + "0"
fx = parse_expr(fx, transformations=transformations)

fx_prime = fx.diff(x)


fx = lambdify(x, fx)
fx_prime = lambdify(x, fx_prime)

value = 0
value2 = 0
k = 0

fx(k)

while value2 == 0:
    if (value >= 0):
        value2 = fx(k)
    else:
        value = fx(k)

    k = k + 1

x_guess = round(random.uniform(value, value2), 1)
# print(fx)

if (method == 'newton'):
    print(newton(fx, fx_prime, x_guess, 1e-8, 10))
elif(method == 'bisection'):
    a = eval(input("Input value of A: "))
    b = eval(input("Input value of B: "))
    print(bisection(fx, a, b, 5))
elif(method == "secant"):
    a = eval(input("Input value of A: "))
    b = eval(input("Input value of B: "))
    print(secant(fx, a, b, 5))
#
#
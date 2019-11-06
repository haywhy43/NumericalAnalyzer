import random
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = (standard_transformations + (implicit_multiplication_application,))

x = Symbol('x')

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

f_of_x = fx(x_guess)
f_prime_of_x = fx_prime(x_guess)
iteration = x_guess


def newton(param):
    new_iteration = param + (fx(param) / fx_prime(param))

    return new_iteration


new_iteration = newton(iteration)

while new_iteration != iteration:
    newton(newton(iteration))
    iteration = new_iteration

print(new_iteration)
print(iteration)

from sympy import *

x = Symbol('x')

f = eval(input("Please input the order of the equation(i.e the highest power in the polynomial): "))
coeffient = []
# f_prime = f.diff(x)
for i in range(f+1):
    coeffient.append(input("Enter Coefficient of order " + format(i) + ": "))



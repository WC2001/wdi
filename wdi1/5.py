import math

def f(x):
    eps = 0.000001
    a = 1.0
    b = x
    while math.fabs(a-b)>=eps:
        a = (a+b)/2.0
        b = x/a
    return a    

x = float(input())

print(round(f(x),6))

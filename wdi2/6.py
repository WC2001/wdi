from math import floor
def f(x):
    a = floor(x**(1/2))
    
    while x%a!=0:
        if x%a==0:
            return a
        a-=1
    return a



n = int(input())
print(f(n),int(n/f(n)))
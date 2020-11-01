def f(n,x):
    if n == 0:
        return x
    else:
        return 1/3 * (2*f(n-1,x)+ x/(f(n-1,x))**2)

x = int(input())

e = 0.0000001

n = 0
while abs(x - f(n,x)**3) > e:
    n+=1
print(round(f(n,x),6))
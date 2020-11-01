x = float(input())
cosx = 1 - x*x/2 + x**4/24 - x**6/720 + x**8/40320

print(round(cosx,6))